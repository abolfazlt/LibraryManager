# Generated by Django 2.0 on 2018-07-25 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EFiles', '0005_efile_file_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='efile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]