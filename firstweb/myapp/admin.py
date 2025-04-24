from django.contrib import admin
from .models import Job, Position, Leave, Profile

admin.site.register(Job)
admin.site.register(Position)
admin.site.register(Leave)
admin.site.register(Profile)
