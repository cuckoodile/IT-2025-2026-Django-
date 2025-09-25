from django.shortcuts import render
from rest_framework.views import APIView
from .models import Subject
from .serializers import SubjectQuerySerializer, SubjectMutationSerializer
from rest_framework.response import Response

# Create your views here.

class SubjectListCreateView(APIView):
    query_set = Subject.objects.all()
    serializer = SubjectQuerySerializer(query_set, many=True)

    def get(self, request):
        data = Subject.objects.all()
        serializer = SubjectQuerySerializer(data, many=True)

        return Response(serializer.data)
        

    def post(self, request):
        data = request.data
        serializer = SubjectQuerySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class SubjectRetrieveUpdateDelete(APIView):

    def get(self, request, pk): # pk = Primary Key
        # Retrieve
        queryset = Subject.objects.get(id=pk)
        # get student where id = 5
        serializer = SubjectQuerySerializer(queryset)

        return Response(serializer.data)
    
    def patch(self, request, pk):
        
        instance = Subject.objects.get(id=pk)

        serializer = SubjectMutationSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({f"Successfully updated: {serializer.data}"})
        
        return Response(serializer.errors)

    def delete(self, request, pk):
        instance = Subject.objects.get(id=pk)

        serializer = SubjectMutationSerializer(instance)

        instance.delete()
        return Response({f"Successfully deleted: {serializer.data}"})