from django.urls import path
from .views import NoteListView, NoteDetailView, CreateNoteView

urlpatterns = [
    path('list/', NoteListView.as_view(), name='note-list'),  # ✅ GET = ดู Note ได้ทุกคน
    path('list/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),  # ✅ GET = ดู Note ได้ทุกคน, PUT/DELETE = เฉพาะเจ้าของ
    path('create/', CreateNoteView.as_view(), name='note-create'),  # ✅ POST = สร้าง Note (ต้องล็อกอิน)
]
