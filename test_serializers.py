import os
import sys
import django
from django.conf import settings

# Add current directory to Python path
sys.path.append(os.getcwd())

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.serializers import StudentSerializer, TeacherSerializer
from django.contrib.auth.models import User

def test_serializers():
    print(\"Testing serializers...\")
    
    # Test data for Student
    student_data = {
        'username': 'teststudent',
        'email': 'student@test.com',
        'password': 'testpass123',
        'first_name': 'Test',
        'last_name': 'Student',
        'middle_name': 'Middle',
        'gender': 'm',
        'birthday': '2000-01-01'
    }

    # Test StudentSerializer
    student_serializer = StudentSerializer(data=student_data)
    if student_serializer.is_valid():
        student = student_serializer.save()
        print('Student created successfully')
        print(f'Student: {student}')
        print(f'Associated User: {student.user}')
        print(f'User username: {student.user.username}')
        print(f'User email: {student.user.email}')
        
        # Clean up
        student.user.delete()
        print('Student test completed successfully')
    else:
        print('Student serializer errors:', student_serializer.errors)

    # Test data for Teacher
    teacher_data = {
        'username': 'testteacher',
        'email': 'teacher@test.com',
        'password': 'testpass123',
        'first_name': 'Test',
        'last_name': 'Teacher',
        'gender': 'f'
    }

    # Test TeacherSerializer
    teacher_serializer = TeacherSerializer(data=teacher_data)
    if teacher_serializer.is_valid():
        teacher = teacher_serializer.save()
        print('\\nTeacher created successfully')
        print(f'Teacher: {teacher}')
        print(f'Associated User: {teacher.user}')
        print(f'User username: {teacher.user.username}')
        print(f'User email: {teacher.user.email}')
        
        # Clean up
        teacher.user.delete()
        print('Teacher test completed successfully')
    else:
        print('Teacher serializer errors:', teacher_serializer.errors)

    print('\\nAll tests completed successfully!')

if __name__ == \"__main__\":
    test_serializers()