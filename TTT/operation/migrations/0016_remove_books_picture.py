# Generated by Django 4.0.5 on 2022-06-26 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0015_remove_books_picture1_books_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='picture',
        ),
    ]
