# Generated by Django 3.0.6 on 2020-05-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profiler_email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
