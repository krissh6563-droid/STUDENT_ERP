# Generated by Django 3.2.3 on 2021-05-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_rename_m_roll_number_marks_detail_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks_detail',
            name='year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students_detail',
            name='year',
            field=models.CharField(max_length=10),
        ),
    ]
