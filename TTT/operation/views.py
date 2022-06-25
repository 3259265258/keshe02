from ctypes.wintypes import HGDIOBJ
from email.mime import image
from pyexpat import model
from tkinter import image_names
from turtle import title
from types import new_class
from urllib import request
from django.conf import settings
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse
from operation.models import books
from operation.utils.uploads import getNewName
import json
import os
# from django import forms
# from operation.utils.bootstrap import BootStrapForm


#测试
# def orm(request):
#     books.objects.create(isbn='98765',bookname="运维部",publishertime='2022-06-21 16:14:19')
#     return HttpResponse("添加成功")


#增加
def add(request):
    isbn1=request.POST.get("isbn")
    bookname1=request.POST.get("bookname")
    publishertime1=request.POST.get("publishertime")
    addlist=books.objects.create(
        isbn=isbn1,
        bookname=bookname1,
        publishertime=publishertime1,

    )
    print(addlist)
    return HttpResponse(json.dumps(addlist),'multipart/form-data')


#全部查询
def query(request):
    qy1=books.objects.all().values()
    data1=list(qy1)
    print(data1)
    return HttpResponse(json.dumps(data1), 'application/json')

#按照id号查询
def select(request):
    nid1=request.GET['id']
    qy2=books.objects.filter(id=nid1).values()
    data2=list(qy2)
    return HttpResponse(json.dumps(data2), 'application/json')

#更新修改
def update(request):
    nid2=request.POST.get('id')
    isbn1=request.POST.get("isbn")
    bookname1=request.POST.get("bookname")
    publishertime1=request.POST.get("publishertime")
    data3=books.objects.filter(id=nid2).update(
        isbn=isbn1,
        bookname=bookname1,
        publishertime=publishertime1
    )
    return HttpResponse(json.dumps(data3), 'application/json')


#删除
def delete(request):
    nid3=request.GET.get('id')
    Del=books.objects.filter(id=nid3).delete()
    print(Del)
    return HttpResponse('删除成功')

def show_avatar(request):
    user = books.objects.filter(name='trent')[0]
    avatarName = str(user.avatar)
    avatarUrl = os.path.join(settings.MEDIA_URL, 'users', avatarName)
    avatar_info = {'userName':'trent', 'avatarUrl': avatarUrl}
    return HttpResponse(json.dumps(avatar_info),'application/json')

def add_user_image(request):
    return render(request)
#上传图片
def upload_handle(request):
    # 获取一个文件管理器对象
    file = request.FILES['pic']
    # 保存文件
    new_name = getNewName('pic') # 具体实现在自己写的uploads.py下
	# 将要保存的地址和文件名称
    where = '%s/users/%s' % (settings.MEDIA_ROOT, new_name)
    # 分块保存image
    content = file.chunks()
    with open(where, 'wb') as f:
        for i in content:
            f.write(i)
    # 上传文件名称到数据库
    books.objects.update(picture=new_name)
    # 返回的httpresponse
    return HttpResponse('ok')