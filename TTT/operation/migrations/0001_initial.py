# Generated by Django 4.0.5 on 2022-06-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=36, verbose_name='图书编号')),
                ('bookname', models.CharField(blank=True, max_length=23, null=True, verbose_name='图书名字')),
                ('publishertime', models.CharField(blank=True, max_length=36, null=True, verbose_name='出版时间')),
            ],
        ),
    ]
