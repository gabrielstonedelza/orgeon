# Generated by Django 3.0.6 on 2020-08-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summerschool', '0009_usersurvey_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersurvey',
            name='improvement',
            field=models.TextField(blank=True, default='Anything that you think we can do to improve our online school sessions.', help_text='Is there something that needs improvement in our summer school?.Give us suggestions'),
        ),
        migrations.AlterField(
            model_name='usersurvey',
            name='something_new',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', help_text='Did your ward enjoy the summer school session?', max_length=4),
        ),
    ]
