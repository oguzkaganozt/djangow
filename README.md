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

Heroku recognizes an app as a Python app by the existence of a Pipfile or requirements.txt file in the root directory.
The Pipfile file lists the app dependencies together with their versions. When an app is deployed, Heroku reads this file and installs the appropriate Python dependencies using the pipenv install --system --skip-lock command.

Heroku apps runs on little container called dynos. Dynos runs cmds listed on Procfile . Different types of dynos avaliable:

https://devcenter.heroku.com/articles/dyno-types#setting-dyno-type

Procfile lists proccess list for heroku to run such as:

    web: gunicorn gettingstarted.wsgi --log-file -
    
To start a heroku remote for an app in (In apps root directory):

    heroku create
    
 To push local app repo to heroku remote (App Deploy to remote):

    git push heroku master
  
Scaling an application on Heroku is equivalent to changing the number of dynos that are running. 
To scale the app by setting active dynos (web=0 means site is offline):

    heroku ps:scale web=1

To check heroku client process list:

    heroku ps

To Run app at localhost in local machine: Simply different procfile for localhost (Procfile.windows=> web: python manage.py runserver 0.0.0.0:5000)

    heroku local web -f Procfile.windows
    
To create virtualenv and install dependencies: Installing dependencies for local machine needed. But once pushed to remote server Heroku auto detects dependencies from pipfile. No cmd's needed for remote server Heroku handles it.

    1. pipenv --three    --> To initiate a virtualenv
    2. pipenv install    --> To instal dependencies to virtualenv 
    3. pipenv shell      --> To activate the virtualenv

To create one-off dyno (just for system operations and used once and killed when Ctrl+C. Like Windows cmd line):

    heroku run -- > "heroku run bash" for open up a bash or "heroku run shell" for open up a python shell
