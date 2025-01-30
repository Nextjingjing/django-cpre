from django.urls import path
from .views import CurriculumList

urlpatterns = [
    path('list/', CurriculumList.as_view(), name='curriculumList-list'),
]