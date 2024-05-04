from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class Member(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='member_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='member_user_permissions')
    memberId = models.CharField(max_length=10)
    borndate = models.CharField(max_length=10)
    Gender = (('M','男性'),('W',"女性"),)
    gender = models.CharField(max_length=5,choices=Gender)
    phoneNum = models.CharField(max_length=10)

    def __str__(self):
        return  self.memberNum
