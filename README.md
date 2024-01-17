

## Instructions

1. Download
2. Extract in a folder
3. Open with visual studio code

### Prerequisites
- Python installed (https://www.python.org/downloads/)
- Django installed (`pip install django`)
- PostgreSQL installed (https://www.postgresql.org/download/)

### Steps

1. **Install PostgreSQL:**
   - Download and install PostgreSQL from the official website.

2. **Create a PostgreSQL Database:**
   - Open the PostgreSQL shell or use a GUI tool like pgAdmin.
   - Create a new database for your Django project.

3. **Install psycopg2:**
   - psycopg2 is the PostgreSQL adapter for Python. Install it using:
     ```
     pip install psycopg2
     ```

4. **Configure Django Settings:**
   - Open your Django project's `settings.py` file.
   - Find the `DATABASES` configuration section.
   - Update the `DATABASES` setting to use PostgreSQL:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations:**
   - Run the following command to apply database migrations:
     ```
     python manage.py migrate
     ```

6. **Test Your Setup:**
   - Create a Django superuser with the following command:
     ```
     python manage.py createsuperuser
     ```
   - Run your Django development server and visit the admin page to verify your setup:
     ```
     python manage.py runserver
     ```
     Open your browser and go to http://127.0.0.1:8000/admin/

7. **Additional Configuration (Optional):**
   - You may want to configure additional settings like time zone, etc., in your `settings.py` file.

8. **Start Building Your App:**
   - Now that your PostgreSQL database is configured, start building your Django app!

### Notes
- Make sure PostgreSQL is running when you start your Django development server.
- Update the placeholders in the `DATABASES` setting with your actual database details.
- Adjust settings based on your production environment and security requirements.

### Resources
- Django documentation: https://docs.djangoproject.com/
- PostgreSQL documentation: https://www.postgresql.org/docs/

Commands:

    py -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    py manage.py runserver


In core /settings.py the stripe is commented out - just put your own details in here (not all of these are connected to the project)

# Stripe Payment
PUBLISHABLE_KEY = ''
SECRET_KEY = ''
STRIPE_ENDPOINT_SECRET = ''

# Admin login
1. http://127.0.0.1:8000/admin
2. username and password = admin# Final_Django
# Final_main_Django
# backup-django
