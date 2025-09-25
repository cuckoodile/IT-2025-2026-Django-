from rest_framework import serializers
from .models import Subject
from student.serializers import StudentListSerializer, CourseSerializer

class SubjectQuerySerializer(serializers.ModelSerializer):
    # Student ser.
    students = StudentListSerializer(many=True, read_only=True)
    # Course ser.
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ["id" , 'name', 'description', 'courses', 'students']
        depth = 1

class SubjectMutationSerializer(serializers.ModelSerializer):
    # Student ser.
    # students = StudentListSerializer(partial=True)
    # Course ser.
    # courses = CourseSerializer(partial=True)

    class Meta:
        model = Subject
        fields = ["id" , 'name', 'description', 'students', 'courses']

    def create(self, validated_data):
        courses = validated_data.pop('courses') # name, description, students
        students = validated_data.pop('students') # name, description

        data = Subject.objects.create(**validated_data)

        data.students.set(students)
        data.courses.set(courses) # or data.courses.set(validated_data['courses'])

        return data
    
    def update(self, instance, validated_data):
        courses = validated_data.pop('courses')
        students = validated_data.pop('students')

        # instance = id 2
        instance.courses.set(courses)
        instance.students.set(students)
        
        return super().update(instance, validated_data)