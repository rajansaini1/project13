from django.db import models

# Create your models here.
class UserRole(models.Model):
    roleid=models.AutoField(primary_key=True)
    rolename=models.CharField(max_length=200,default="")
    isActive=models.BooleanField(default=True)
class SiteUser(models.Model):
    roleid=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    userFullName=models.CharField(max_length=200,default="")
    userEmail = models.CharField(primary_key=True,max_length=200, default="")
    userPassword = models.CharField(max_length=200, default="")
    userMobile = models.BigIntegerField()
    isActive=models.BooleanField(default=True)

class UserPhoto(models.Model):
    roleid=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    userFullName=models.CharField(max_length=200,default="")
    userEmail = models.CharField(primary_key=True,max_length=200, default="")
    userPassword = models.CharField(max_length=200, default="")
    photo = models.CharField(max_length=200, default="")
    userMobile = models.BigIntegerField()
    isActive=models.BooleanField(default=True)
