from django.db import models
from django.contrib.auth.models import *
from django.conf import settings
#會員
class Member(AbstractUser):
    borndate = models.CharField(max_length=10, default='')
    # borndate = models.DateField(null=True, blank=True)
    Gender = (('M','男性'),('W',"女性"),)
    gender = models.CharField(max_length=5,choices=Gender)
    # phoneNum = models.CharField(max_length=10)
    phoneNum = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):#看你要顯示啥 所以有可能是他的錯
        return  str(self.id)

#產品資料
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', default='default.jpg')  # 定義默認值
    price = models.CharField(max_length=20,default='0')
    color = models.CharField(max_length=20,default='商品顏色')
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=10,default="man")

    def __str__(self):
        return self.name

#庫存
class InventoryChange(models.Model):
    CHANGE_TYPES = (
    ('increase', '增加'),
    ('decrease', '減少'),
    ('adjustment', '調整'),
)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)#產品編號 是外鍵
    size = models.CharField(max_length=20,default='商品尺寸')
    price = models.CharField(max_length=20,default='0')
    color = models.CharField(max_length=20,default='商品顏色')
    quantity = models.IntegerField(default=0)
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPES,default='increase')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):##
        return f"{self.product_id.name} - 尺寸: {self.size}, 颜色: {self.color}, 價格: {self.price}, 數量: {self.quantity}, 變更類型: {self.get_change_type_display()}"

#購物車
class shoppingCart(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)#on_delete=models.CASCADE 就是檢查參照完整性
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    orderQua = models.CharField(max_length=10,default=0)

    def __str__(self):
        return f"購物車編號: {self.id} - 會員: {self.member_id.username} - 產品: {self.product_id.name} - 數量: {self.orderQua}"

#訂單
class Order(models.Model):
    Send_Method =(
    ('7-11pick', '7-11取貨'),
    ('homepick', '店到家宅配'),
    ('familypick', '全家取貨'),
)   
    Pay_Method =(
    ('7-11pick', '現金'),
    ('homepick', '信用卡'),
) 
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True)
    totPrice = models.CharField(max_length=10)
    send = models.CharField(max_length=10, choices=Send_Method)
    pay = models.CharField(max_length=10, choices=Pay_Method)
    def __str__(self):
        return str(self.id)
#訂單明細
class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    totQua = models.CharField(max_length=10)

#評論資料
class Comment(models.Model):
    Score = (
    ('onestar', '★'),
    ('twostar', '★★'),
    ('threestar', '★★★'),
    ('fourstar', '★★★★'),
    ('fivestar', '★★★★★'),
)   
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    score = models.IntegerField(choices=Score)
    scoreDate = models.DateTimeField(auto_now_add=True)