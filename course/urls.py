from django.urls import path
from .views import CourseList, CourseDetail

urlpatterns = [
    path('list/', CourseList.as_view(), name='course-list'),
    path('list/<id>/', CourseDetail.as_view(), name='course-detail'),
]