Simple API for Invoice Management:

This is a simple Django-based API for managing invoices and their details. The API supports the creation and updating of invoices, including associated invoice details (products/services), through a single request.

Features:

Create Invoice: Create a new invoice along with multiple invoice details (items).
Update Invoice: Update an existing invoice and replace the old details with the new ones provided.
Invoice Details: Each invoice can have multiple invoice details (description, quantity, price, and line total).
GET Invoices: Fetch all invoices and their details.



Assumptions Made During Implementation:

Single Invoice: Each invoice contains multiple invoice details. When updating an invoice, the old details are replaced with the new ones.
Invoice Validation: When updating an invoice, if the invoice number already exists, the existing invoice is updated.
Data Validation: If any required fields are missing from the request, appropriate error messages are returned to the user.
No Authentication: This API doesn't currently implement authentication or authorization. It's assumed that any user can access and modify invoice data.
Primary Key (pk): The Invoice model uses the primary key (pk) to identify each invoice for update operations.


Requirements:

Before running this project, you need to have the following installed:
Python 3.8+
Django 5.0+
Django REST Framework
Other dependencies (listed in requirements.txt)



Setup Instructions:

Clone the repository:
git clone https://github.com/yourusername/your-repository-name.git](https://github.com/manmathshanti/neura_dynamic-simple_api
cd neura_dynamic-simple_api

Install dependencies: Install the required libraries using pip:
pip install -r requirements.txt

Apply migrations: Make sure to apply the migrations to set up the database.
python manage.py migrate


Run the development server: Start the server to test the API locally:
python manage.py runserver



Access the API: The API will be available at http://127.0.0.1:8000/.

To create an invoice, make a POST request to /api/invoices/.
To update an invoice, make a PUT request to /api/invoices/.
To fetch all invoices, make a GET request to /api/invoices/.
