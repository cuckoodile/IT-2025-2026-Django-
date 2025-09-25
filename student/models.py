from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, validators=[
        MinLengthValidator(3, "First name must be atleast 3 characters")
    ])
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True , null=True)

    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

