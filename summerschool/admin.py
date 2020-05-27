from django.contrib import admin
from .models import School, Student, SchoolLoginCode, SchoolKid

admin.site.register(School)
admin.site.register(Student)
admin.site.register(SchoolLoginCode)
admin.site.register(SchoolKid)
