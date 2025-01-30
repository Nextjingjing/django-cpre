from django.urls import path
from .views import CourseList, CourseDetail, CourseSearch

urlpatterns = [
    path('list/', CourseList.as_view(), name='course-list'),
    path('list/<id>/', CourseDetail.as_view(), name='course-detail'),
    path('search/<str:search>/', CourseSearch.as_view(), name='course-search'),
]