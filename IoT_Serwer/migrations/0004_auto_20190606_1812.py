# Generated by Django 2.2.1 on 2019-06-06 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Serwer', '0003_auto_20190601_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentstatedata',
            name='shutterState',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
