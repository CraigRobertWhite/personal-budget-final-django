# Generated by Django 3.1.4 on 2020-12-19 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0006_unique_constraints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_expenses',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
