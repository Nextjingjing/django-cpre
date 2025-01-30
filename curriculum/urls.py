from django.urls import path
from .views import CurriculumList, CurriculumDetail

urlpatterns = [
    path('list/', CurriculumList.as_view(), name='curriculumList-list'),
    path('list/<id>/', CurriculumDetail.as_view(), name='curriculum-detail'),
]