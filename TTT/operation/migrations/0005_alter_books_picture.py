# Generated by Django 4.0.5 on 2022-06-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_books_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.CharField(max_length=255, verbose_name='图片'),
        ),
    ]
