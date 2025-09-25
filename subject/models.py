from django.db import models
from student.models import Course, Student

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    courses = models.ManyToManyField(Course, related_name='subjects')
    students = models.ManyToManyField(Student, related_name='subjects')