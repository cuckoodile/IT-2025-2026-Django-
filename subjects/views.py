# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from core.permissions import *
from .models import Subject
from .serializers import SubjectSerializer

# Create your views here.
# Subject Views (with restrictions)
class SubjectListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]  # Admins/Teachers create? But for now admin

    def get(self, request):
        subjects = Subject.objects.all()
        # Optional: Filter for students to see only their course subjects
        if hasattr(request.user, 'student_profile'):
            student = request.user.student_profile
            subjects = subjects.filter(courses__in=student.courses.all()).distinct()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            # Set teacher if user is teacher
            if hasattr(request.user, 'teacher_profile'):
                serializer.save(teacher=request.user.teacher_profile)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetailedView(APIView):
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Teacher modifies, others view

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subject = self.get_object(pk)
        self.check_object_permissions(request, subject)
        # For students, check if in their courses (restriction)
        if hasattr(request.user, 'student_profile'):
            student = request.user.student_profile
            if not subject.courses.filter(id__in=student.courses.values_list('id', flat=True)).exists():
                return Response({"detail": "Not allowed to view this subject."}, status=status.HTTP_403_FORBIDDEN)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        subject = self.get_object(pk)
        self.check_object_permissions(request, subject)
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        self.check_object_permissions(request, subject)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)