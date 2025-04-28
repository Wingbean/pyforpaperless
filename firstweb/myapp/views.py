from django.shortcuts import render, redirect, get_object_or_404 # add redirect
from django.http import HttpResponse # add line
from .models import Job, Profile, Job_detail # add line จาก models.py นำ class Job, class อื่น ๆ เข้ามา
from django.contrib.auth.models import User # add line นำ User จาก authen เข้ามา
from django.contrib.auth import authenticate, login , logout # เรียกใช้การ authen จาก auth
from django.contrib import messages # เรียกใช้ message
from django.contrib.auth.decorators import login_required # use login required in model

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

        # add to Job_detail
        newdetail = Job_detail()
        newdetail.job = newjob
        newdetail.description = '-'
        newdetail.save()

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

            return redirect("login") # ให้ redirect กลับไปหน้า login ตอนแรกเป็น home
        
        else:
            context["user_taken"] = True #เพื่อแจ้งเตือนว่า email มีการสมัครเรียบร้อยแล้ว
    
    return render(request, 'myapp/register.html', context)

def user_login(request):
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password) #ตรวจสอบว่ามี user นี้ไหม
        print(user, "User")
        
        if user is not None: # แปลว่ามี user จริง
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'email หรือ Password ไม่ถูกต้อง !!!')
    return render(request, 'myapp/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'ออกจากระบบสำเร็จ')
    return redirect('login') # ให้กลับไปหน้า login

@login_required # เพิ่มเข้ามาเพื่อให้ต้อง login ก่อน ถึงจะโชว์ model นี้
def table_job(request):
    # if ไม่ให้เข้า จนกว่า user type จะเป็น admin
    if request.user.profile.user_type != 'admin':
        return redirect('home')
    job = Job.objects.all()
    context = {'job' :job}
    return render(request, 'myapp/tablejob.html',context) #แนบ context เข้าไปเพื่อ for loop

# filter job ฒา id เดียว เลย
def detail_job(request, id):
        
    job = Job.objects.get(id=id) # เราจะได้ job ที่เป็น Id นั้นออกมา
    # เพิ่มการรับข้อมูล จากการ กด submit ในหน้า detail-job
    if request.method == 'POST':
        data = request.POST.copy()
        description = data.get('description')
        yesno = data.get('yesno')
        print('description: ', description)
        print('yesno: ', yesno)
        detailjob = Job_detail.objects.get(job=job)
        detailjob.description = description
        detailjob.yesno = yesno
        detailjob.save()

    detailjob = Job_detail.objects.get(job=job)
    context = {'job' : job, 'detailjob' : detailjob} # เก็บเป็น context ส่งไปหน้า html
    return render(request, 'myapp/detail-job.html', context)

# สร้างการ แก้ไข job
def edit_job(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        data = request.POST.copy()
        fullname = data.get('fullname')
        tel = data.get('tel')
        position = data.get('position')
        
        job.fullname = fullname
        job.tel = tel
        job.position = position
        job.save()