from django.contrib import admin
from mysite.models import Member,Product,InventoryChange
from django.contrib import admin


class MemberAdmin(admin.ModelAdmin):
    list_display=['username','id','borndate','gender','phoneNum']

admin.site.register(Member,MemberAdmin)
admin.site.register(Product)
admin.site.register(InventoryChange)