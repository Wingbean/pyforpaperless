from django.urls import path
from .views import Home, register, user_login, user_logout
# ใน folder เดียวกัน ช่วยหา views.py ให้หน่อย แล้ว import Fn Home() เข้ามา

# ข้างล่างเป็นตัวกำหนดทางเดินของเวบ
urlpatterns = [
    path('', Home, name='home'), #path('') มันก็คือ localhost:8000
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
