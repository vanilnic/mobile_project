# Generated by Django 5.0.6 on 2024-06-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0014_expinc_categori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]