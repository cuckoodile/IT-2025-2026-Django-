# Setting up Django Project

1. **create directory**
```sh
mkdir <name_of_folder>
```

2. **go inside your directory.**
```sh
cd <name_of_directory>
```

3. **create virtual environment**
```sh
python -m venv venv
```

4. **activate your virtual env.**
```sh
venv\Scripts\activate
```

5. **Install django**
```sh
pip install django
```

6. **check the dependencies**
```sh
pip freeze
```

7. **save the dependencies to** `requirements.txt`
```sh
pip freeze > requirements.txt
```

8. **create django project.**
```sh
django-admin startproject core .
```

9. **run django development server**
```sh
python manage.py runserver
```

    `ctrl + c` to stop the server

10. **create apps**
```sh
python manage.py startapp student
```

11. **add your new app to installed app** List
`settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student', # add your new app
]
```

12. create a model
`models.py`
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True , null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

13. register your model to adminpanel
`admin.py`
```python
from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)
```

## create super user account
```sh
python manage.py createsuperuser
```

## migrations command
```sh
python manage.py makemigrations
python manage.py migrate
```

## run server
```sh
python manage.py runserver
```

## test your code.
`127.0.0.1:8000/admin`

