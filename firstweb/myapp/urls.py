from django.urls import path
from .views import Home # ใน folder เดียวกัน ช่วยหา views.py ให้หน่อย แล้ว import Fn Home() เข้ามา

# ข้างล่างเป็นตัวกำหนดทางเดินของเวบ
urlpatterns = [
    path('', Home), #path('') มันก็คือ localhost:8000
]