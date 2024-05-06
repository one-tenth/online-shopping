from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class Member(AbstractUser):
    borndate = models.CharField(max_length=10)
    Gender = (('M','男性'),('W',"女性"),)
    gender = models.CharField(max_length=5,choices=Gender)
    phoneNum = models.CharField(max_length=10)

    def __str__(self):
        return  self.gender
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
class InventoryChange(models.Model):
    CHANGE_TYPES = (
    ('increase', '增加'),
    ('decrease', '减少'),
    ('adjustment', '调整'),
)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=20,default='商品尺寸')
    price = models.CharField(max_length=20,default='0')
    color = models.CharField(max_length=20,default='商品顏色')
    quantity = models.IntegerField()
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - 尺寸: {self.size}, 颜色: {self.color}, 價格: {self.price}, 數量: {self.quantity}, 變更類型: {self.get_change_type_display()}"
