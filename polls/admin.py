from django.contrib import admin

from .models import Question, Choice

# Register your models here.
# 管理员账号：zzy，密码：zzy979481894
admin.site.register(Question)
admin.site.register(Choice)
