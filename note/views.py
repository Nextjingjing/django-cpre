from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



# ✅ ให้ทุกคน (แม้ไม่ล็อกอิน) ดู Note ได้
class NoteListView(generics.ListAPIView):
    """
    - **GET**: ทุกคนสามารถดูรายการ Note ได้
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]  # ✅ ทุกคนดูได้

class CreateNoteView(APIView):
    """
    - **POST**: สร้าง Note (ต้องล็อกอิน)
    {
"name": "Example Note",
"link": "https://www.example.com"
    }

    """
    permission_classes = [IsAuthenticated]  # ✅ ต้องล็อกอินถึงจะสร้างได้

    def post(self, request):
        """สร้าง Note ถ้าเข้าด้วย POST"""
        serializer = NoteSerializer(data=request.data, context={'request': request})  # ✅ ส่ง context ให้ serializer
        if serializer.is_valid():
            serializer.save()  # ✅ `account` จะถูกกำหนดจาก `request.user` อัตโนมัติ
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ ให้เฉพาะเจ้าของ Note แก้ไข/ลบ Note ได้
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    - **GET**: ทุกคนสามารถดู Note ได้ (แม้ไม่ล็อกอิน)
    - **PUT/PATCH/DELETE**: เฉพาะเจ้าของโน้ตเท่านั้นที่สามารถแก้ไขหรือลบได้
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ คนไม่ล็อกอินดูได้ แต่แก้ไข/ลบไม่ได้

    def get_object(self):
        """
        - **ให้เฉพาะเจ้าของสามารถแก้ไข/ลบได้**
        - **แต่ทุกคนยังสามารถดู (GET) ได้**
        """
        note = super().get_object()
        if self.request.method in ["PUT", "PATCH", "DELETE"]:  # ✅ ป้องกันคนที่ไม่ใช่เจ้าของ
            if note.account != self.request.user:
                raise PermissionDenied("You do not have permission to modify or delete this note.")
        return note
