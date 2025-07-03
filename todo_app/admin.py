from django.contrib import admin
from .models import User_Tasks,completed_tasks
# Register your models here.
admin.site.register(User_Tasks)
admin.site.register(completed_tasks)