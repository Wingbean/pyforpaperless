from django.db import models
from django.contrib.auth.models import User # นำเข้า User เข้ามาใช้

class Job(models.Model):
    fullname = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    # ทำให้หลังจาก เพิ่มข้อมูลใน form มันจะแสดงเป็นชื่อ fullname
    # ไม่ต้อง makemigration
    def __str__(self):
        return self.fullname

class Position(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(default=10000) # ค่าเริ่มต้น 10000
    manager = models.CharField(max_length=255) #ใครเป็นผู้จัดการ
    description = models.TextField(null=True, blank=True) #ไม่บังคับกรอก
    
    def __str__(self):
        return self.title

class Leave(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    sdate = models.DateField()
    ldate = models.DateField()

    def __str__(self):
        return self.fname + ' ' + self.lname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #เรียกใช้ user
    user_type = models.CharField(max_length=20, default= 'employee')
    bio = models.CharField(max_length=255)
    facebook = models.CharField(max_length=100, default= 'No Facebook')
    tel = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user
