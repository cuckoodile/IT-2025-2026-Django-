# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Teacher, Course

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id', 'middle_name', 'gender', 'birthday', 'age', 'username', 'email', 'password', 'first_name', 'last_name', 'courses', 'subjects']
        read_only_fields = ['age']  # age auto-calculated

    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        
        # Extract many-to-many fields
        courses = validated_data.pop('courses', [])
        subjects = validated_data.pop('subjects', [])
        
        # Remove 'user' key if it exists in validated_data to avoid conflicts
        validated_data.pop('user', None)

        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create the student with the associated user (excluding many-to-many fields)
        student = Student.objects.create(user=user, **validated_data)
        
        # Now set the many-to-many relationships
        if courses:
            student.courses.set(courses)
        if subjects:
            student.subjects.set(subjects)
            
        return student

class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'gender', 'username', 'email', 'password', 'first_name', 'last_name']
        # read_only_fields = []

    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')

        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create the teacher with the associated user
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'