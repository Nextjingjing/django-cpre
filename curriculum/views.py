from django.shortcuts import render
from .serializers import CurriculumSerializer
from .models import Curriculum , CurriculumMapping
from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.
class CurriculumList(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

class CurriculumDetail(generics.RetrieveAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    lookup_field = 'id'

class CurriculumLatestView(APIView):
    """ 🔹 Get the latest curriculum and its courses """
    def get(self, request):
        last_curriculum = Curriculum.objects.order_by("-id").first()
        if not last_curriculum:
            return JsonResponse({"error": "No curriculum found"}, status=404)

        courses = last_curriculum.curriculum_mappings.all()
        data = [
            {"id": cm.course.id, "name": cm.course.name, "year": cm.course.year, "term": cm.course.term}
            for cm in courses
        ]
        return JsonResponse({"curriculum": last_curriculum.name, "courses": data}, safe=False)