from django.shortcuts import render, redirect # add redirect
from django.http import HttpResponse # add line
from .models import Job, Profile # add line จาก models.py นำ class Job, class อื่น ๆ เข้ามา
from django.contrib.auth.models import User # add line นำ User จาก authen เข้ามา

# start create fn for myapp\urls.py

def Home(request):
    if request.method == 'POST' : 
        data = request.POST.copy() # data เป็น Dict ที่มาจากการ submit form
        print('DATA: ', data)
        fullname = data.get('fullname')
        tel = data.get('tel')
        position = data.get('position')
        print('Fullname: ', fullname)
        print('Tel: ', tel)
        print('position: ', position)
        # ดึง model Job มา save ของที่ submit เข้ามา
        newjob = Job()
        newjob.fullname = fullname
        newjob.tel = tel
        newjob.position = position
        newjob.save() #ใช้ method save() ที่ inherit มาจาก "from django.db import models"

    #return HttpResponse('<h1>Hello World from DataSloth</h1>')
    return render(request, 'myapp/home.html')

def register(request):
    context = {}
    if request.method == 'POST' :
        data = request.POST.copy() #copy ข้อมูลที่ส่งมาจากฟอร์ม , data เป็น Dict ที่มาจากการ submit form
        
        print('DATA: ', data)

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        print('Username: ', name)
        print('Password: ', password)
        print('Email: ', email)

        checK_user = User.objects.filter(username=email)

        if not checK_user.exists():
            new_user = User(username=email, first_name=name)
            new_user.set_password(password)
            new_user.save()

            profile = Profile(user=new_user) #p เล็ก ตัวแปร P คือโมเดล
            profile.save()

            context['success'] = True # เพื่อระบุว่าการลงทะเบียนสำเร็จ

            return redirect("home") # ให้ redirect กลับไปหน้า login
        
        else:
            context["user_taken"] = True #เพื่อแจ้งเตือนว่า email มีการสมัครเรียบร้อยแล้ว
    
    return render(request, 'myapp/register.html', context)