# Bank Branch API

This Django project provides a RESTful API for querying bank and branch details. It also includes a custom Django management command to populate the branch data from a CSV file into the PostgreSQL database.

## Project Structure

- **bank/models.py**: Contains the models `Bank` and `Branch`.
- **bank/serializers.py**: Serializers to convert model instances to JSON format for API responses.
- **bank/views.py**: API views for handling requests to the endpoints.
- **bank/urls.py**: URL routing for the API endpoints.
- **bank/management/commands/pop.py**: Custom Django management command to populate branch data from a CSV file.
- **manage.py**: Django's command-line utility.
- **db.sqlite3**: (Optional) Default SQLite database used during development.

## Models

### Bank

- **id**: Primary key, BigInteger.
- **name**: CharField, max length 49.

### Branch

- **ifsc**: Primary key, CharField, max length 11.
- **bank_id**: ForeignKey, related to `Bank`.
- **branch**: CharField, max length 74.
- **address**: CharField, max length 195.
- **city**: CharField, max length 50.
- **district**: CharField, max length 50.
- **state**: CharField, max length 26.

## API Endpoints

### REST API

1. **API Root**
   - **URL**: `/`
   - **Method**: GET
   - **Description**: Returns the list of available endpoints.

2. **List Banks**
   - **URL**: `/banks/`
   - **Method**: GET
   - **Description**: Returns a list of all banks.

3. **Bank Details**
   - **URL**: `/banks/<int:pk>/`
   - **Method**: GET
   - **Description**: Returns details of a specific bank along with its branches.

4. **List Branches**
   - **URL**: `/branches/`
   - **Method**: GET
   - **Description**: Returns a list of all branches.

5. **Branch Details**
   - **URL**: `/branches/<str:ifsc>/`
   - **Method**: GET
   - **Description**: Returns details of a specific branch.

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- Django 4.2+
- Django REST Framework

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/bank-branch-api.git
   cd bank-branch-api

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt

4. **Setup PostgreSQL:**

    Create a PostgreSQL database and configure your `DATABASES` setting in `settings.py`
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'bank_data',  # Replace with your database name
                'USER': 'postgres',  # Replace with your PostgreSQL username
                'PASSWORD': 'yourpassword',  # Replace with your PostgreSQL password
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }

    Apply migrations:
        ```bash
        python manage.py migrate

5. **Run the development server:**

    ```bash
    python manage.py runserver

6. **Access the API:**
    Visit `http://127.0.0.1:8000/` in your browser or use a tool like Postman to interact with the API.


### Populating Data

You can populate the `Branch` model from a CSV file using the custom management command `pop`.

1. **Place your CSV file containing branch data in the desired location and update the file path in the `pop.py` command file:**

    csv_file_path = '/path/to/your/csv/file.csv'

2. **Run the management command:**
    python manage.py pop
    This command will read the CSV file and populate the Branch model with the data.