from django.urls import path
from .views import CurriculumList, CurriculumDetail, CurriculumLatestView

urlpatterns = [
    path('list/', CurriculumList.as_view(), name='curriculumList-list'),
    path('list/<id>/', CurriculumDetail.as_view(), name='curriculum-detail'),
    path('latest/', CurriculumLatestView.as_view(), name='curriculum-latest'),
]