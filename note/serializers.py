from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())  # ✅ ใช้ request.user อัตโนมัติ
    account_username = serializers.ReadOnlyField(source='account.username')  # ✅ แสดงชื่อ user แทน ID

    class Meta:
        model = Note
        fields = ['id', 'name', 'link', 'account', 'account_username', 'created_at', 'updated_at']
