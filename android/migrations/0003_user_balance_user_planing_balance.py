# Generated by Django 5.0.6 on 2024-06-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0002_categories_limitations'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='planing_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]