# Generated by Django 4.1.5 on 2023-02-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
