# Bank API - RESTful API for Bank and Branch Details

This project provides a RESTful API service for querying bank and branch details. It was developed using Django and Django REST Framework, with data stored in an SQLite database. The project was originally designed to use PostgreSQL, but due to free-tier limitations on PythonAnywhere, SQLite was used instead. The project has been successfully deployed on PythonAnywhere [https://apurvapandit.pythonanywhere.com/].

## Features
- **REST API Endpoints**:
  - `/api/banks/`: Retrieve a list of all banks.
  - `/api/banks/<pk>/`: Retrieve details for a specific bank by its primary key (ID).
  - `/api/branches/`: Retrieve a list of all branches.
  - `/api/branches/<ifsc>/`: Retrieve details for a specific branch by its IFSC code.
- **Data Import**: Management commands (`pop.py` and `stats.py`) for populating the database with banks and branches from CSV files.
- **Clean Code**: The project adheres to best practices and clean coding principles.

## How to Run the Project Locally

1. **Clone the Repository**:
    ```bash
    git clone <your-repo-link>
    cd <your-repo-directory>
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Populate the Database**:
    - Add bank data: 
      ```bash
      python manage.py stats
      ```
    - Add branch data:
      ```bash
      python manage.py pop
      ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the API**:
    Open your web browser and go to `http://127.0.0.1:8000/` to start using the API.

## Deployment on PythonAnywhere

The project has been deployed on PythonAnywhere. Below are the key steps:

1. **Set Up a PythonAnywhere Account**:
    - Create an account on PythonAnywhere and create a new web app.
    - Choose the Django framework and the appropriate Python version.

2. **Upload Your Project Files**:
    - Use the PythonAnywhere file browser to upload your project files or use Git to clone your repository.

3. **Install Requirements**:
    - In the PythonAnywhere console, navigate to your virtual environment and install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

4. **Database Configuration**:
    - Since PostgreSQL is a paid feature on PythonAnywhere, the database was switched to SQLite. The necessary changes were made in `settings.py`.

5. **Collect Static Files**:
    ```bash
    python manage.py collectstatic
    ```

6. **Reload the Web App**:
    - Finally, reload the web app from the PythonAnywhere dashboard.

## Time Taken

This assignment was completed within 1 day.

## Notes

- PostgreSQL was initially considered, but due to limitations on PythonAnywhere's free tier, SQLite was used instead.