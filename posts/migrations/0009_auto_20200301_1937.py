# Generated by Django 3.0.3 on 2020-03-01 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200301_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AddField(
            model_name='form',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]