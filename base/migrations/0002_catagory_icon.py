# Generated by Django 5.0.1 on 2024-01-03 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='category_icons/', validators=[django.core.validators.FileExtensionValidator(['png'])]),
        ),
    ]
