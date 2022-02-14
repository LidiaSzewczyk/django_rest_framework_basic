# Installation
* mkdir drf
* cd drf
* mkvirtualenv drf / pipenv shell /
* pip install django django-debug-toolbar djangorestframework drf-yasg
* django-admin startproject config .
* python manage.py startapp users
* python manage.py runserver


## debug_toolbar
settings.py
INSTALLED_APPS = [...
    "debug_toolbar", ...]
MIDDLEWARE = [...
    'debug_toolbar.middleware.DebugToolbarMiddleware', ...]
INTERNAL_IPS = [
    "127.0.0.1",]
urls.py