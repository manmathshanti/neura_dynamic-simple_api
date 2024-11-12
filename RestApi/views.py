from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.exceptions import ValidationError

class InvoiceView(APIView):
    def post(self, request):
        return self.create_or_update_invoice(request)
    
    def put(self, request):
        return self.create_or_update_invoice(request)
    
    def create_or_update_invoice(self, request):
        invoice_number = request.data.get("invoice_number")
        if not invoice_number:
            return Response(
                {"error": "invoice_number is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Try to find an existing invoice by `invoice_number`
            invoice = Invoice.objects.filter(invoice_number=invoice_number).first()
            
            if invoice:
                # If invoice exists, update it
                serializer = InvoiceSerializer(invoice, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(
                        {"message": "Invoice updated successfully", "data": serializer.data},
                        status=status.HTTP_200_OK
                    )
            else:
                # If no invoice is found, create a new one
                serializer = InvoiceSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(
                        {"message": "Invoice created successfully", "data": serializer.data},
                        status=status.HTTP_201_CREATED
                    )

        except IntegrityError:
            return Response(
                {"error": "An integrity error occurred. Please check your data and try again."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValidationError as e:
            return Response(
                {"error": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"error": "An unknown error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    def get(self, request):
        # Retrieve all invoices
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
