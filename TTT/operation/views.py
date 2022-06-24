from ctypes.wintypes import HGDIOBJ
from email.mime import image
from pyexpat import model
from tkinter import image_names
from turtle import title
from django.conf import settings
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse
from operation.models import books
import json
import os
from django import forms
from operation.utils.bootstrap import BootStrapForm
# from django import forms
# Create your views here.

#测试
# def orm(request):
#     books.objects.create(isbn='98765',bookname="运维部",publishertime='2022-06-21 16:14:19')
#     return HttpResponse("添加成功")

class UpForm(forms.Form):
    isbn=forms.CharField(label='书籍编号')
    booknamen=forms.CharField(label='书籍名字')
    publishertime=forms.CharField(label='出版日期')
    img=forms.FileField(label='图片')


#增加
def add(request):
    form=UpForm(data=request.POST,files=request.FILES)
    isbn1=request.POST.get("isbn")
    bookname1=request.POST.get("bookname")
    publishertime1=request.POST.get("publishertime")
    if form.is_valid():
        img_obj=form.changed_data.POST.get("media")
        file_path=os.path.join("operation","static","media",img_obj.name)
        f=open(file_path,mode='wb')
        for chunk in img_obj.chunks():
            f.write(chunk)
        f.close()
        addlist=books.objects.create(
            isbn=isbn1,
            bookname=bookname1,
            publishertime=publishertime1,
            picture=file_path,
        )
    # print(addlist)
    return HttpResponse("上传成功")

    # isbn1=request.POST.get("isbn")
    # bookname1=request.POST.get("bookname")
    # publishertime1=request.POST.get("publishertime")
    # addlist=books.objects.create(
    #     isbn=isbn1,
    #     bookname=bookname1,
    #     publishertime=publishertime1,
    # )
    # print(addlist)
    # return HttpResponse("添加成功")
    

#全部查询
def query(request):
    # offset=int(request.GET.get('offset'))
    # pagesize=int(request.GET.get('pagesize'))
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


#上传图片
def picture(request):
    if request.method=='POST':
        img_obj=request.FILES.get("test.shlian")
        f=open(os.path.join(settings.MEDIA_ROOT,"upload",img_obj.name),'wb')
        for chunk in img_obj.chunks():
            f.write(chunk)
        f.close()
        result={"result":"OK","filename":img_obj.name,"media_root":os.path.join(settings.MEDIA_ROOT,"upload")}
    return HttpResponse(result)

    # print(request)
    # file=request.FILES['name']
    # print(file)
    # root='%s/%s'%(settings.PICTURE,file.name)
    # with open(root,'wb') as f:
    #     for i in file.chunks():
    #         f.write(i)
    
    
# def photo(request):
#     if request.method=='POST':
#         new_img=books(
#             photo=request.FILES.get('photo'),
#             user=request.FILES.get('photo').name
#         )
#         new_img.save()
#     return HttpResponse('上传成功')


# def upload(request):
#     f1=request.FILES.get('picture')
#     p=Pictures()
#     p.pic="booktest/"+f1.name
#     p.save()
#     fname=settings.MEDIA_ROOT+"/booktest/"+f1.name
#     with open(fname,"wb") as pic:
#         for c in f1.chunks():
#             pic.write(c)
#     return HttpResponse("上传成功")
# def show_pic(request):
#     nid4=request.POST.get("id")
#     pic_obj=Pictures.objects.get(id=nid4)
#     return HttpResponse(json.dumps(pic_obj),'application/json')