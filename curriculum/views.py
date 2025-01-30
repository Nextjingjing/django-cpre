from django.shortcuts import render
from .serializers import CurriculumSerializer
from .models import Curriculum
from rest_framework import generics

# Create your views here.
class CurriculumList(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

class CurriculumDetail(generics.RetrieveAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    lookup_field = 'id'