# DjangoProject My_Movies

## Description

show a list of my favorite movies with rating stars, project that i did learning django

## Getting Started

### Prerequisites

- Python (version 3.11)
- Django 

### Installation

1. Clone the repository:

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # For Windows, use "venv\Scripts\activate"

3. Install the required packages:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate

5. Create a superuser (if you plan to use the Django Admin):

python manage.py createsuperu

6. Collect static files (if needed):

python manage.py collectstatic

### Usage
To start the development server, run:

python manage.py runserver
The application will be available at http://localhost:8000/.

If you created a superuser, you can access the Django Admin at http://localhost:8000/admin/ to manage the data.
