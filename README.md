## New and Old book Purchase System (Web Application) 
## Overview

This web application, built on the Django framework and utilizing PostgreSQL as the database, is designed to create a comprehensive platform for the buying and selling of both new and used books. The primary focus is to enable users to seamlessly transition from being readers to sellers, creating a dynamic marketplace for literary enthusiasts. The application embraces a user-centric approach, providing a range of features to enhance the overall book-buying and selling experience.

### Key Features

1. **User Account Management:**
   - Readers can easily create and manage their accounts, personalizing their experience on the platform.

2. **Book Catalog and Purchase:**
   - A rich catalog allows users to explore and purchase a diverse range of books, whether new or used.

3. **Order Tracking:**
   - Users can conveniently track the status of their book orders, ensuring transparency and convenience.

4. **Secure Payment Processing:**
   - A robust and secure payment system is integrated to facilitate safe and hassle-free transactions.

5. **Book Upload for Sale:**
   - Sellers can effortlessly upload books they wish to sell, expanding the platform into a two-way marketplace.

6. **Historical Tracking:**
   - Users have access to a comprehensive history of their transactions and interactions on the platform.

7. **Feedback and Rating System:**
   - A dynamic feedback system allows users to share their thoughts, contributing to a community-driven rating system.

8. **Reader Discussions:**
   - A dedicated space for literary discussions fosters a sense of community among users with shared interests.

### Technology Stack

- **Backend:**
  - Developed using Python with the Django framework.

- **Database:**
  - PostgreSQL is employed as the primary database to ensure robust and scalable data management.

- **Frontend:**
  - HTML, JavaScript, CSS, and Bootstrap for an intuitive and responsive user interface.

### Additional Feature

An in-built blog app is included to encourage users to engage in discussions, share recommendations, and contribute to a thriving literary community.

This Bookstore Web Application aspires to provide a seamless and enriching experience for book enthusiasts, bridging the gap between readers and sellers in an interactive and user-friendly environment.

## Setting up PostgreSQL with Django

## Prerequisites
- Python installed (https://www.python.org/downloads/)
- Django installed (`pip install django`)
- PostgreSQL installed (https://www.postgresql.org/download/)

## Instructions

1. **Download:**
   - Download the project and extract it into a folder.

2. **Open with Visual Studio Code:**
   - Open the project folder with Visual Studio Code.

3. **Create and Activate Virtual Environment:**
   - Open a terminal in Visual Studio Code.
   - Run the following commands:
     ```bash
     # Create a virtual environment
     py -m venv venv

     # Activate the virtual environment
     venv\Scripts\activate
     ```

4. **Install Dependencies:**
   - With the virtual environment activated, run:
     ```bash
     pip install -r requirements.txt
     ```

5. **Install PostgreSQL:**
   - Download and install PostgreSQL from the official website.

6. **Create a PostgreSQL Database:**
   - Open the PostgreSQL shell or use a GUI tool like pgAdmin.
   - Create a new database for your Django project.

7. **Install psycopg2:**
   - psycopg2 is the PostgreSQL adapter for Python. Install it using:
     ```bash
     pip install psycopg2
     ```

8. **Configure Django Settings:**
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

9. **Apply Migrations:**
   - Run the following commands to apply database migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

10. **Test Your Setup:**
    - Create a Django superuser:
      ```bash
      python manage.py createsuperuser
      ```
    - Run the Django development server:
      ```bash
      py manage.py runserver
      ```
    - Visit the admin page in your browser (http://127.0.0.1:8000/admin/) to verify your setup.

11. **Additional Configuration (Optional):**
    - Uncomment the Stripe configuration in `core/settings.py` and add your own details.

12. **Start Building Your App:**
    - With everything set up, start building your Django app!

## Commands
- To activate the virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux).
- To run the development server: `py manage.py runserver`.

## Packages
- Django
- Black
- isort
- django-mptt
- Pillow
- Stripe
- Coverage
- Six
- django-countries

## Notes
- Make sure PostgreSQL is running when you start your Django development server.
- Update the placeholders in the `DATABASES` setting with your actual database details.
- Adjust settings based on your production environment and security requirements.

## Resources
- Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- PostgreSQL documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)


# Testing

## Unit Tests and PyTest

The Bookstore Web Application has undergone a rigorous testing process to ensure reliability, functionality, and code quality. The testing strategy includes both unit tests and PyTest to cover various aspects of the application.

### Unit Tests

Unit tests have been implemented to validate the functionality of individual components or units within the application. These tests focus on ensuring that each part of the codebase performs as intended in isolation, adhering to the principles of modularity and encapsulation.

To run unit tests, use the following command:

```bash
python manage.py test


# Stripe Payment Integration

## Setting Up Stripe Payment in Your Django Project

To enable Stripe payment functionality in your Django project, follow these steps:

1. **Set Up Stripe Account:**
   - Create an account on [Stripe](https://stripe.com/) if you don't have one.

2. **Retrieve API Keys:**
   - After logging into your Stripe account, navigate to the Dashboard and access the Developers section to obtain your Publishable Key and Secret Key.

3. **Configure Django Settings:**
   - Open your Django project's settings file (`settings.py`).
   - Add the following lines and replace the placeholders with your Stripe API keys:

   ```python
   # settings.py

   STRIPE_PAYMENT_SETTINGS = {
       'PUBLISHABLE_KEY': 'your_publishable_key',
       'SECRET_KEY': 'your_secret_key',
       'STRIPE_ENDPOINT_SECRET': 'your_stripe_endpoint_secret',
   }
    'STRIPE_ENDPOINT_SECRET': 'your_stripe_endpoint_secret',
   }



