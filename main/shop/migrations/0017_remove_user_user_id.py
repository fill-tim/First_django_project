# Generated by Django 4.1.5 on 2023-02-05 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]