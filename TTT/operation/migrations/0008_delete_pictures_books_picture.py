# Generated by Django 4.0.5 on 2022-06-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_pictures_delete_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pictures',
        ),
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(default='user1.jpg', upload_to='pictures'),
        ),
    ]