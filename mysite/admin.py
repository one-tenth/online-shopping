from django.contrib import admin
from mysite.models import Member,Product,InventoryChange,shoppingCart,Order,OrderDetail,Comment
from django.contrib import admin


class MemberAdmin(admin.ModelAdmin):
    list_display=['username','id','borndate','gender','phoneNum']#id是會員編號

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','image','quantity']

class InventoryChangeAdmin(admin.ModelAdmin):
    list_display=['product_id','size','quantity','gender','timestamp']

class shoppingCartAdmin(admin.ModelAdmin):
    list_display=['member_id','id','product_id','orderQua']#id是購物車編號

class OrderAdmin(admin.ModelAdmin):
    list_display=['member_id','id','orderDate','totPrice']#id是訂單編號

class OrderDetailAdmin(admin.ModelAdmin):
    list_display=['order_id','product_id','totQua']

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','member_id','order_id','comment','score']
admin.site.register(Member,MemberAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(InventoryChange)
admin.site.register(shoppingCart,shoppingCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
admin.site.register(Comment,CommentAdmin)