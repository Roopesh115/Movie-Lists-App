# Generated by Django 4.2.15 on 2024-08-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]