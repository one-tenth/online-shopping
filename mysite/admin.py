from django.contrib import admin
from mysite.models import Member
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    list_display=['username','borndate','gender','phoneNum']

admin.site.register(Member,MemberAdmin)
