# Generated by Django 3.0.6 on 2020-08-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summerschool', '0008_usersurvey'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersurvey',
            name='ratings',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, help_text='How would you rate our summer school?', max_length=3),
        ),
    ]