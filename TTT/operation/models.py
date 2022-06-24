from email.policy import default
from django.db import models

# Create your models here.
class books(models.Model):
    id=models.AutoField(primary_key=True)
    isbn=models.CharField(max_length=255,verbose_name='图书编号')
    bookname=models.CharField(max_length=255,verbose_name='图书名字')
    publishertime=models.CharField(max_length=255,verbose_name='出版时间')
    # user=models.CharField(max_length=64)
    picture=models.CharField(max_length=255,verbose_name='头像')
    