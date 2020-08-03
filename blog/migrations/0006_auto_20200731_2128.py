# Generated by Django 3.0.6 on 2020-07-31 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200731_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersurvey',
            name='participate',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', help_text='Would you participate again if organized next time?', max_length=4),
        ),
        migrations.AddField(
            model_name='usersurvey',
            name='recommend',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', help_text='Would you recommend a friend next time?', max_length=4),
        ),
        migrations.AddField(
            model_name='usersurvey',
            name='something_new',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', help_text='Did your ward learn something new?', max_length=4),
        ),
    ]
