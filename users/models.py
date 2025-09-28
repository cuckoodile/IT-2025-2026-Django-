from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from subjects.models import Subject

class Student(models.Model):
    GENDER_CHOICES = [
        ("m", "male"),
        ("f", "female"),
    ]
    
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    courses = models.ManyToManyField('Course', related_name='students')
    subjects = models.ManyToManyField('subjects.Subject', related_name='enrolled_students')

    def save(self, *args, **kwargs):
        if self.birthday:
            today = date.today()
            self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Student"

class Teacher(models.Model):
    GENDER_CHOICES = [
        ("m", "male"),
        ("f", "female"),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')

    def __str__(self):
        return f"{self.user.username} - Teacher"

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name