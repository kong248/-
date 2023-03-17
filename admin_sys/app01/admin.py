from django.contrib import admin

# Register your models here.
# 注册部门表到amin界面
from django.contrib import admin

from .models import Department, UserInfo

admin.site.register(Department)
admin.site.register(UserInfo)