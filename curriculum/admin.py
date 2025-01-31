from django.contrib import admin
from .models import Curriculum, CurriculumMapping


# Register our model
admin.site.register(Curriculum)
admin.site.register(CurriculumMapping)