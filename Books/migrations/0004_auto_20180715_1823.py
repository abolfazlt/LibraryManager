# Generated by Django 2.0.7 on 2018-07-15 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_book_taken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='taken',
            new_name='is_taken',
        ),
    ]
