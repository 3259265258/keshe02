# Generated by Django 4.0.5 on 2022-06-25 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0011_books_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='avatar',
            new_name='picture',
        ),
    ]
