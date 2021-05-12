# Generated by Django 3.1.7 on 2021-05-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_patient_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='risk',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=25),
        ),
    ]