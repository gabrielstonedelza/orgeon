# Generated by Django 3.0.6 on 2020-08-03 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200802_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_file',
            field=models.ImageField(blank=True, upload_to='post_posters', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]),
        ),
    ]
