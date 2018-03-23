# djangow
Smooth web development with Django

Django is WEB development framework for Python
Main principal of it is The MVT(Model-View-Template) like MVC(Model View Controller)

General design steps of a Django-site:

    0. Create a django project and create an app using manage.py
    1. First step of backend is URL design: We do it so by adding paths to urls.py
    2. Then mapping each route to a view.
    3. Views designed as simple functions
    4. Views should return an appropriate HTTP response to corresponding URL request.
    5. URL->View->Model->Template->HTTP Response
    
To start the django project run from terminal:

    'django-admin startproject mysite'
    
To start an app in django project run from terminal:

    'python manage.py startapp polls'
    
To run the django development server run from terminal:

    'python manage.py runserver'

To create migration scripts for models to database(django will auto create or alter changes for DB ) run from terminal:

    'python manage.py makemigrations APPNAME'
    
To apply the migration scripts to database run from terminal:

    'python manage.py migrate'
    
To open up a great shell for interacting with models:

    'python manage.py shell'
    
To create admin users for interacting with models using site/admin:

    'python manage.py createsuperuser MYADMIN'
 
    



    
    
