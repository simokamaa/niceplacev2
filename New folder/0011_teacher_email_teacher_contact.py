# Generated by Django 4.2.1 on 2023-09-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_teaching_subjects_teacher_teaching_units_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
