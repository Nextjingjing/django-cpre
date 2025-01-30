from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics

# Create your views here.
class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # return Response(queryset.data)