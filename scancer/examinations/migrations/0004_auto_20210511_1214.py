# Generated by Django 3.1.7 on 2021-05-11 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examinations', '0003_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examinations.examination'),
        ),
    ]
