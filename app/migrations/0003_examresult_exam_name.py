# Generated by Django 4.2.1 on 2023-09-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_attendance_student_delete_elearning_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='exam_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
