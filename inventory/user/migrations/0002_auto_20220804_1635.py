# Generated by Django 2.1.7 on 2022-08-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/avatar.jpg', upload_to='Profile_Images'),
        ),
    ]