from django.contrib import admin
from mysite.models import Member,Product,InventoryChange,shoppingCart
from django.contrib import admin


class MemberAdmin(admin.ModelAdmin):
    list_display=['username','id','borndate','gender','phoneNum']

class shoppingCartAdmin(admin.ModelAdmin):
    list_display=['member_id','id','product_id','orderQua']

admin.site.register(Member,MemberAdmin)
admin.site.register(Product)
admin.site.register(InventoryChange)
admin.site.register(shoppingCart,shoppingCartAdmin)