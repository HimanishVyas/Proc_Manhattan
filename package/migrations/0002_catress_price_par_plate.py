# Generated by Django 4.2.4 on 2023-09-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catress',
            name='price_par_plate',
            field=models.FloatField(default=1, verbose_name='Price Par Plate'),
            preserve_default=False,
        ),
    ]
