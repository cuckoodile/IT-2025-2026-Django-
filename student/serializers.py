from rest_framework import serializers
from .models import Student, Course
# from subject.serializers import SubjectQuerySerializer

class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "middle_name", "course", "subjects"]
        depth = 2

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id" , 'first_name' , 'last_name' , 'middle_name', 'course']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields = ['id', 'name']
        fields = "__all__"
        