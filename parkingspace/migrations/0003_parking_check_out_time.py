# Generated by Django 5.0 on 2023-12-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingspace', '0002_parking_check_out_alter_parking_parking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='check_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
