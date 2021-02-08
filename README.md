# Demo web forum

## Introduction
This is a web forum app built with Django that allows users to create accounts, reset passwords,
view boards, topics and posts as well as create the same. See a live demo at: demoboards.henga.co

## Installation
NOTE: This project assumes you have python 3.6 installed as well as virtualenv. It also assumes you
have a local version of postgres installed with a database called 

1. Download/Clone the repository to your local machine
2. In the same parent folder as the repo folder, create a virtual environment with the command: `virtualenv venv -p python3`
3. Your parent folder structure should have the following folders
    - django-forum-example
    - venv
4. Initialize the virtual environment: `source venv/bin/activate`
5. Enter the django-forum-example folder and install all requirements: `pip install -r requirements.txt`
6. Create a .env file within the django-forum-example folder with the following variables:
    - SECRET_KEY=your_app_secret
    - DEBUG=True
    - ALLOWED_HOSTS=.localhost,127.0.0.1
    - EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
    - DATABASE_URL=postgresql://postgres:postgres@localhost:5432/demoboards
    - RECAPTCHA_PUBLIC_KEY=your_key
    - RECAPTCHA_PRIVATE_KEY=your_key
    NOTE: This project uses google captcha. You can create your own recaptcha keys from the Google captcha
    site: https://www.google.com/recaptcha/about/
7. Run the migrations: `python manage.py migrate`
8. Run the app: `python manage.py runserver`

This project also makes use of `django_crontab` for running a cron script that continuously clears data to prevent spam
entries. To get that running you can run the command `python manage.py crontab add`.
You can learn more about `django_crontab` commands from the docs: https://pypi.org/project/django-crontab/