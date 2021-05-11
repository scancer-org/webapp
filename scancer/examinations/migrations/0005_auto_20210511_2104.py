# Generated by Django 3.1.7 on 2021-05-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examinations', '0004_auto_20210511_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='kind',
            field=models.CharField(choices=[('manual', 'Manual Exam'), ('mammogram', 'Mammogram'), ('ultrasound', 'Ultrasound'), ('mri', 'MRI'), ('biopsy', 'Lymph Node Biopsy')], max_length=25),
        ),
    ]
