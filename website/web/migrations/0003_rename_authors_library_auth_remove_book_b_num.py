# Generated by Django 5.0.2 on 2024-02-27 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_library'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='Authors',
            new_name='auth',
        ),
        migrations.RemoveField(
            model_name='book',
            name='b_num',
        ),
    ]
