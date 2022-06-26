from django.contrib import admin
from operation.models import books    #导入数据库表模型
from django.contrib import admin
@admin.register(books)
class ArticleAdmin(admin.ModelAdmin):
    #list_display表示：设置可显示的字段
    list_display = ('id','isbn','bookname','publishertime')
admin.site.site_header='我的后台'
admin.site.unregister(books)
admin.site.register(books,ArticleAdmin)       #把数据库表注册到后台中显示 