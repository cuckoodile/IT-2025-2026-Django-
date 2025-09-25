from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student, Course
from .serializers import StudentListSerializer, StudentCreateSerializer, CourseSerializer
from rest_framework.response import Response

# Create your views here.
class StudentView(APIView):
    # model.object.query
    def get(self, request):
        # List of Student model
        queryset = Student.objects.all()
        serializer = StudentListSerializer(queryset , many=True)

        return Response(serializer.data)

    def post(self, request):
        def sanitizer(value = str):
            if not isinstance(value, str):
                raise TypeError("Input must be a string")
                
            # Replace multiple spaces with a single space
            value = " ".join(value.split())
            
            # Apply title case and strip whitespace
            return value.title().strip()

        data = request.data
        
        data['first_name'] = sanitizer(data['first_name'])
        data['last_name'] = sanitizer(data['last_name'])
        data['middle_name'] = sanitizer(data['middle_name'])

        serializer = StudentCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

class StudentRetrieveUpdateDelete(APIView):

    def get(self, request, pk): # pk = Primary Key
        # Retrieve
        queryset = Student.objects.get(id=pk)
        # get student where id = 5
        serializer = StudentListSerializer(queryset)

        return Response(serializer.data)
    
    def patch(self, request, pk):
        
        instance = Student.objects.get(id=pk)

        serializer = StudentCreateSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({f"Successfully updated: {serializer.data}"})
        
        return Response(serializer.errors)

    def delete(self, request, pk):
        instance = Student.objects.get(id=pk)

        serializer = StudentCreateSerializer(instance)

        instance.delete()
        return Response({f"Successfully deleted: {serializer.data}"})
    
class CourseView(APIView):
    # model.object.query
    def get(self, request):
        # List of Student model
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset , many=True)

        return Response(serializer.data)

    def post(self, request):
        def sanitizer(value = str):
            if not isinstance(value, str):
                raise TypeError("Input must be a string")
            # Information     TECHNOLOGY
            # Information Technology
                
            # Replace multiple spaces with a single space
            value = " ".join(value.split())
            
            # Apply title case and strip whitespace
            return value.title().strip()

        data = request.data
        
        data['name'] = sanitizer(data['name'])

        serializer = StudentCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)