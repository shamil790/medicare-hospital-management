# Generated by Django 3.2.10 on 2023-02-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
