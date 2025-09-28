from django.db import models
from users.models import Student, Teacher, Course

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    
    students = models.ManyToManyField(Student, related_name='enrolled_subjects', blank=True)
    courses = models.ManyToManyField(Course, related_name='subjects')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name