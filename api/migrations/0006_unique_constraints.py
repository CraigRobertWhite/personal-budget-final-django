# Generated by Django 3.1.4 on 2020-12-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0005_unique_user_accounts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={},
        ),
        migrations.AlterModelOptions(
            name='monthlyexpense',
            options={},
        ),
        migrations.AddConstraint(
            model_name='goal',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_user_goals'),
        ),
        migrations.AddConstraint(
            model_name='monthlyexpense',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_user_expenses'),
        ),
    ]
