# Installation
* mkdir drf
* cd drf
* mkvirtualenv drf / pipenv shell /
* pip install django django-debug-toolbar djangorestframework drf-yasg
* django-admin startproject config .
* python manage.py startapp users
* python manage.py runserver


## First step - django rest framework, debug_toolbar, swagger, CustomUser
* settings.py
```python
INSTALLED_APPS = [...
    'debug_toolbar',
    'rest_framework',
    'drf_yasg',
                  
    'users.apps.UsersConfig',
...]
MIDDLEWARE = [...
    'debug_toolbar.middleware.DebugToolbarMiddleware', ...]
INTERNAL_IPS = [
    "127.0.0.1",]
AUTH_USER_MODEL = 'users.CustomUser'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]}
```
* urls.py
* users/models.py, users/admin.py
* *python manage.py makemigrations
* *python manage.py migrate