from django.contrib import admin
from .models import Passport, UserInfo, Group, Transmission, Model, Brand, Car, \
    Instructor, FormatLearning, ProgramLearning, Student

admin.site.register(Passport)
admin.site.register(UserInfo)
admin.site.register(Group)
admin.site.register(Transmission)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Instructor)
admin.site.register(FormatLearning)
admin.site.register(ProgramLearning)
admin.site.register(Student)
