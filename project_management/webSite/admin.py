from django.contrib import admin
from .models import Student, Professor, Semester, Industry, Grade, Notification


# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Semester)
admin.site.register(Industry)
admin.site.register(Grade)
admin.site.register(Notification)
