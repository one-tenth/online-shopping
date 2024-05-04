from django.contrib import admin
from mysite.models import Member
from django.contrib import admin
from mysite import models

class MemberAdmin(admin.ModelAdmin):
    list_display=['memberId','borndate','gender','phoneNum']

admin.site.register(Member,MemberAdmin)