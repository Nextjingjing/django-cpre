# 🚀 Django Google OAuth API

Django REST Framework API ที่รองรับการล็อกอินผ่าน Google OAuth และใช้ `.env` สำหรับเก็บค่าคอนฟิก

## 📌 Features
✅ รองรับ **Google OAuth Login**  
✅ ใช้ **Django REST Framework** สำหรับ API Authentication  
✅ ใช้ **Token Authentication** สำหรับการเข้าถึง API  
✅ ใช้ **`python-dotenv`** เพื่อจัดการค่าคอนฟิกจาก `.env`  
✅ รองรับ **Browsable API UI** สำหรับทดสอบ API ใน Browser  
✅ รองรับการ **Deploy บน Production** ด้วย `Gunicorn` และ `NGINX`  

---

## 🔧 **การติดตั้ง (Installation)**
### 1️⃣ **Clone โปรเจค**
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
2️⃣ สร้าง Virtual Environment
sh
คัดลอก
แก้ไข
python -m venv venv
source venv/bin/activate  # สำหรับ macOS/Linux
venv\Scripts\activate     # สำหรับ Windows
3️⃣ ติดตั้ง dependencies
sh
คัดลอก
แก้ไข
pip install -r requirements.txt
4️⃣ ตั้งค่า .env
คัดลอกไฟล์ .env.example เป็น .env

sh
คัดลอก
แก้ไข
cp .env.example .env
จากนั้นเปิดไฟล์ .env แล้วใส่ค่าจริงสำหรับ Google OAuth:

env
คัดลอก
แก้ไข
SECRET_KEY="your-secret-key-here"
DEBUG=True

GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
GOOGLE_REDIRECT_URI="http://127.0.0.1:8000/accounts/google/login/callback/"
5️⃣ รันการ Migrate Database
sh
คัดลอก
แก้ไข
python manage.py migrate
6️⃣ สร้าง Superuser (สำหรับเข้า Admin)
sh
คัดลอก
แก้ไข
python manage.py createsuperuser
กรอก Username, Email และ Password ตามต้องการ

7️⃣ รันเซิร์ฟเวอร์
sh
คัดลอก
แก้ไข
python manage.py runserver
เปิด Browser และเข้าไปที่ http://127.0.0.1:8000/admin/
เพื่อเข้าใช้งาน Django Admin Panel