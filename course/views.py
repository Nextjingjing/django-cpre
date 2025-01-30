from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics

# Create your views here.
class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # return Response(queryset.data)

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'

class CourseSearch(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        search_query = self.kwargs.get('search', None)
        if search_query:
            queryset = queryset.filter(name__startswith=search_query)
        return queryset