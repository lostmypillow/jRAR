# Generated by Django 5.0.6 on 2024-06-03 14:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_rename_success_requestattempt_succeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestattempt',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
