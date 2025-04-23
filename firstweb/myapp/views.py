from django.shortcuts import render
from django.http import HttpResponse # add line
from .models import Job # add line จาก models.py นำ class Job เข้ามา

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