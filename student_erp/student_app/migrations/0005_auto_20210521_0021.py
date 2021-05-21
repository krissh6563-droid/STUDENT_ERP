# Generated by Django 3.2.3 on 2021-05-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_auto_20210521_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks_detail',
            old_name='pre_exam_1',
            new_name='obtained_marks',
        ),
        migrations.RenameField(
            model_name='marks_detail',
            old_name='pre_exam_2',
            new_name='total_marks',
        ),
        migrations.RemoveField(
            model_name='marks_detail',
            name='unit_1',
        ),
        migrations.RemoveField(
            model_name='marks_detail',
            name='unit_2',
        ),
        migrations.RemoveField(
            model_name='marks_detail',
            name='unit_3',
        ),
        migrations.RemoveField(
            model_name='marks_detail',
            name='unit_4',
        ),
        migrations.AddField(
            model_name='marks_detail',
            name='exam_type',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
