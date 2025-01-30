from django.contrib import admin
from .models import Course, CurriculumMapping


# Register our model
admin.site.register(Course)
admin.site.register(CurriculumMapping)