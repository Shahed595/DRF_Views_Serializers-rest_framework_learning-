from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

from rest_framework import generics,viewsets


# class StudentListCreateView(generics.ListCreateAPIView):#get,post
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerilizers


# class StudentRetrieveUpdateDestroView(generics.RetrieveUpdateDestroyAPIView):#get,put, delete
#     queryset = models.StudentData.objects.all()
#     serializer_class = serializers.StudentSerilizers

#recommended (This just 3 line codes allow to grt, create,put,patch,delete)
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerilizers

class CourseListCreateView(generics.ListCreateAPIView):#get,post
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseRetrieveUpdateDestroView(generics.RetrieveUpdateDestroyAPIView):#get,put, delete
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

# class StudentView(APIView):
#     def get(self, request, format=None):
#         studentData = models.StudentData.objects.all()
#         serializer = serializers.StudentSerilizers(studentData, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = serializers.StudentSerilizers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerilizers(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerilizers(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)