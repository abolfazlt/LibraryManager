# Generated by Django 2.0 on 2018-07-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0012_remove_book_book_logo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_logo',
            field=models.ImageField(default='', max_length=500, upload_to=''),
        ),
    ]