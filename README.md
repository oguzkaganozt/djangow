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
 
    
# heroku

Heroku apps runs on little container called dynos. Dynos runs cmds listed on Procfile . Different types of dynos avaliable:

'Dyno Type	Sleeps	Professional Features	Memory (RAM)	CPU Share	Dedicated	Compute
free	        yes	        no	                512 MB	        1x	        no	    1x-4x
hobby	        no	        no	                512 MB	        1x	        no	    1x-4x
standard-1x	    no	        yes	                512 MB	        1x	        no	    1x-4x
standard-2x	    no	        yes	                1024 MB	        2x	        no	    4x-8x
performance-m	no	        yes	                2.5 GB	        100%	    yes	    11x
performance-l	no	        yes	                14 GB	        100%	    yes	    46x'

Procfile lists proccess list for heroku to run such as:

    web: gunicorn gettingstarted.wsgi --log-file -
    
To start a heroku remote for an app in (In apps root directory):

    heroku create
    
 To push local app repo to heroku remote (App Deploy to remote):

    git push heroku master
  
To scale the app by setting active dynos (web=0 means site is offline):

    heroku ps:scale web=1

To check heroku client process list:

    heroku ps
    
