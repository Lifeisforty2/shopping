# Project Setup Instructions

## Prereqs
    Make sure you have the following installed:
    - Python 3.8 or higher
    - pip 

## Environment Setup

1. **Clone the Repo**
    ...
    git clone https://reopurl/shopping_project.git
    cd shopping_project
    ...

2. **Create and Activate a Virtual Environment (optional)**
    Windows:
    ...
    python -m venv venv
    venv\Scripts\activate
    ...
    Mac:
    ...
    python3 -m venv venv
    source /venv/bin/activate
    ...

3. **Install Requirements**
    ...
    pip install -r requirements.txt
    ...

## Database Setup

1. **Migrate Database ()**
    Run the folliwing command to create the database schema.
    ...
    Python manage.py migrate
    ...
2. **Create Superuser**
    an administrative user that allows you to add data through the admin interface
    ...
    python manage.py createsuperuser
    ...
3. **Run the Development Server**
    ...
    python manage.py runserver
    ...
4. **Access the App**
    open your web browser and go to 'http://127.0.0.1:8000/'.

## Using the Django Interface
To add or modify the data:
1. Go to 'http://127.0.0.1:8000/admin/' and log in using the superuser account you made.
2. navigate to the relevant section (e.g., Products) to add, edit or remove items.
