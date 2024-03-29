# Generated by Django 3.0.6 on 2020-08-01 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_notifyme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='poster',
        ),
        migrations.AddField(
            model_name='post',
            name='post_doc',
            field=models.FileField(blank=True, help_text="Allowed ['docx', 'doc', 'pdf', 'txt', 'odt', 'rtf', 'tex', 'wpd', 'ods ', 'xls', 'xlsm', 'xlsx', 'pptx', 'ppt', 'pps', 'odp']", upload_to='post_documents', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['docx', 'doc', 'pdf', 'txt', 'odt', 'rtf', 'tex', 'wpd', 'ods ', 'xls', 'xlsm', 'xlsx', 'pptx', 'ppt', 'pps', 'odp'])]),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_doc',
            field=models.FileField(blank=True, help_text="Allowed ['docx', 'doc', 'pdf', 'txt', 'odt', 'rtf', 'tex', 'wpd', 'ods ', 'xls', 'xlsm', 'xlsx', 'pptx', 'ppt', 'pps', 'odp']", upload_to='report_documents', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['docx', 'doc', 'pdf', 'txt', 'odt', 'rtf', 'tex', 'wpd', 'ods ', 'xls', 'xlsm', 'xlsx', 'pptx', 'ppt', 'pps', 'odp'])]),
        ),
    ]
