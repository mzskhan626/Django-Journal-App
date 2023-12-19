# Django-Journal-App

Django Journal App is a web application built with Django that serves as an online journal system. It allows users to keep track of information they've learned about different topics.

## Features

- User authentication and authorization
- Topic and entry management
- Integration with Django admin for easy data entry
- ...

## Getting Started

To set up this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mzskhan626/Django-Journal-App.git
   cd learning-log
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` in your web browser to view the application.
