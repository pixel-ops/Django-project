# Generated by Django 4.1.7 on 2023-03-17 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_multiple_images_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiple_images',
            name='image',
            field=models.FileField(upload_to='myimg'),
        ),
    ]
