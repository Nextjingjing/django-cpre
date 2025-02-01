from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # ใช้ get_user_model() เพื่อรองรับ Custom User Model

class Note(models.Model):
    name = models.CharField(max_length=255)  # ชื่อของโน้ต
    link = models.URLField(unique=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")  # เชื่อมกับ User
    created_at = models.DateTimeField(auto_now_add=True)  # เวลาสร้าง
    updated_at = models.DateTimeField(auto_now=True)  # เวลาอัปเดตล่าสุด

    def __str__(self):
        return f"{self.name} - {self.account.username}"
