# Generated by Django 4.2.1 on 2023-09-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_staff_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]