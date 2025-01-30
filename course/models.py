from django.db import models
from curriculum.models import Curriculum


# Create your models here.
class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    term = models.IntegerField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.id} - {self.name}"
    
class CurriculumMapping(models.Model):  
    curriculum = models.ForeignKey(
        Curriculum, 
        on_delete=models.CASCADE, 
        related_name="curriculum_mappings"
    )  
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name="curriculum_mappings"
    )  

    class Meta:
        verbose_name = "Curriculum Mapping"
        verbose_name_plural = "Curriculum Mappings"
        unique_together = ('curriculum', 'course')  # ป้องกันการเพิ่มซ้ำ

    def __str__(self):
        return f"{self.curriculum.name} - {self.course.name}"