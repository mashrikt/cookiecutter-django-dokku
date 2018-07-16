<p align="center">
  <a href="#"><img src="/media/django-dokku.png" height=100/></a>
</p>

<h1 align="center">
  Cookiecutter Django Dokku
</h1>
<p align="center">
  A framework for jumpstarting Django projects and deploying with Dokku.
</p>
<br/>

Instead of using django-admin startproject to start a new Django application from scratch, you can use this cookiecutter project to start with a Dockerized application ready for Dokku deployment. Some additional common Django features like an extended User model with Email as identification token field, setting up restframework, etc can also be initialized during the initial project set up.

Dokku is a mini-Heroku, powered by Docker. It simplifies the process of building and managing the lifestyle of applications. Once Dokku is set up in a host, you can push codes via Git, just like Heroku. 

Instructions below specify how to start your project from this cookiecutter template and also a guideline on how to set up Dokku on your server. 

## Requirements

* [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
* [Docker](https://docs.docker.com/install/)
* [Docker Compose]( https://docs.docker.com/compose/install/)


### Set Up A Project
```
cookiecutter gh:mashrikt/cookiecutter-django-dokku
```
![Alt text](/media/terminalsession.png)
```
cd myproject
docker-compose up --build
```


## Features

* [Postgres Database](https://www.postgresql.org/)

* [Whitenoise](http://whitenoise.evans.io/en/stable/) for static file serving

* [Gunicorn](http://gunicorn.org/), Python WSGI HTTP Server


## Optional Integrations
*These can be setup during the initial project integration*

[Email User](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#substituting-a-custom-user-model)

* Django by default ships with username as the identification token field. (ie. login with username)
Select 'y' to email _user for using email instead through an extended User model in your myproject.users app.


[Celery](http://www.celeryproject.org/)

* Select 'y' to use_celery for Celery with a Redis backend for Distributed Task Queue.


[Sentry](https://sentry.io):

* To configure sentry you have to add the SENTRY_DSN_URL and
initialize it with your own DSN URL that sentry provides for your django project.

```
dokku config:set myproject SENTRY_DSN_URL=MYSENTRYDSNURL
```

[Django REST framework](http://www.django-rest-framework.org/):

* Django REST framework is a powerful and flexible toolkit for building Web APIs.
Select 'y' to use_rest_framework prompt for this library.


[django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/)

* If you chose to use_rest_framework, you can also opt for REST authentication endpoints.
Since we consider testing mandatory, hence these APIs ship with a few basic test cases written with pytest.


[Restframework Docs](http://www.django-rest-framework.org/topics/documenting-your-api/)

* Again, if you're using Restframework, you can plug in the Restframework Docs as well.


### Setting up Dokku on a Linux Server
```
# install the latest stable version of dokku
wget https://raw.githubusercontent.com/dokku/dokku/v0.12.10/bootstrap.sh;
sudo DOKKU_TAG=v0.12.10 bash bootstrap.sh

# Once the installation is complete, you can open a browser to setup your SSH key and virtualhost settings. 
# Open your browser and navigate to the host's IP address - or the domain you assigned to that IP previously
# Configure Dokku via the web admin.

# create the app
dokku apps:create myproject

# Set environtment variable for ALLOWED_HOSTS. 
# YOUR_HOST is the host's IP address - or the domain you assigned to that IP
dokku config:set ALLOWED_HOSTS=YOUR_HOST

# install the postgres plugin
sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git

# create a postgres service
dokku postgres:create myproject-database

# link postgres service to the app
dokku postgres:link myproject-database myproject

# if your're using Celery, you need to setup Redis
# install the redis plugin
sudo dokku plugin:install https://github.com/dokku/dokku-redis.git redis

# create a redis service
dokku redis:create myproject-redis

# link postgres service to the app
dokku redis:link myproject-redis myproject

```

### Deploying the app from your local machine
```
# add remote dokku url 
git remote add dokku dokku@dokku.me:myproject

# push your apllication 
git push dokku master
```

## Reference
* [Dokku Installation](https://github.com/dokku/dokku/blob/master/docs/getting-started/installation.md)
* [Dokku Redis](https://github.com/dokku/dokku-redis)
* [Dokku Application Deployment](http://dokku.viewdocs.io/dokku/deployment/application-deployment/)


## License

   MIT License
