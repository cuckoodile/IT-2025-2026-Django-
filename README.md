# Django Project Creation Guide

This guide provides step-by-step instructions for creating a new Django project with Django REST Framework.

## Steps

1. **Create a project folder**  
   Create a new folder for your project.

2. **Navigate to the folder**  
   Open the created folder in your terminal or use the command:  
   ```
   cd {created_folder_name}
   ```

3. **Create a virtual environment**  
   ```
   python -m venv venv
   ```

4. **Activate the virtual environment**  
   On Windows:  
   ```
   venv\Scripts\activate
   ```  
   (Note: If you're on macOS/Linux, use `source venv/bin/activate` instead.)

5. **Install dependencies**  
   ```
   pip install django djangorestframework
   ```  
   Add more dependencies if needed, e.g., `pip install django djangorestframework some-other-package`.

6. **Start the Django project**  
   ```
   django-admin startproject core .
   ```

7. **Create a Django app**  
   ```
   python manage.py startapp {app_name}
   ```

8. **Update settings.py**  
   Open `core/settings.py` and add the following to the `INSTALLED_APPS` list:  
   ```
   'rest_framework',
   '{app_name}',
   ```  
   Add other dependencies as needed, e.g., `'{other_dependency}',`.

9. **Make migrations**  
   ```
   python manage.py makemigrations
   ```

10. **Apply migrations**  
    ```
    python manage.py migrate
    ```

11. **Run the server**  
    ```
    python manage.py runserver
    ```