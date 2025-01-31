from django.urls import path
from .views import CurriculumList, CurriculumDetail, CurriculumLatestView, CurriculumCoursesView

urlpatterns = [
    path('list/', CurriculumList.as_view(), name='curriculumList-list'),
    path('list/<id>/', CurriculumDetail.as_view(), name='curriculum-detail'),
    path('latest/', CurriculumLatestView.as_view(), name='curriculum-latest'),
    path("<str:curriculum_id>/course/", CurriculumCoursesView.as_view(), name="curriculum-courses"),
]