# Generated by Django 4.1.5 on 2023-02-11 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_remove_group_student_id_student_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='timetable_id',
        ),
        migrations.AddField(
            model_name='timetable',
            name='group_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.timetable'),
            preserve_default=False,
        ),
    ]
