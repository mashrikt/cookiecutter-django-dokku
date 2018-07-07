# Cookiecutter Django Dokku
A simple boilerplate for using Dokku with Django, Postgres and Celery(Redis backend)


**_Django_** The Web framework for perfectionists with deadlines.

**_Dokku_** A docker-powered PaaS that helps you build and manage the lifecycle of applications

The two together can be a handy and powerful combination for rapidly developing and safely maintaining production ready applications.


**_cookiecutter-django-dokku_**
A framework for jumpstarting production-ready Django projects and deploying with Dokku.


## Requirements

* [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
* [Docker](https://docs.docker.com/install/)
* [Docker Compose]( https://docs.docker.com/compose/install/)
    
    
### Run Project Locally
```
cookiecutter gh:mashrikt/cookiecutter-django-dokku
```
![Alt text](/media/terminalsession.png)
```
cd myproject
docker-compose up --build
```

### Setting up Dokku in a Linux Server
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

## Optional Integrations
*These can be setup during the initial project integration*

[Sentry](https://sentry.io):

* To configure sentry you have to add the SENTRY_DSN_URL and 
initialize it with your own DSN URL that sentry provides for your django project.


## License

MIT License
