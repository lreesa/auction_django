# Generated by Django 2.2.6 on 2019-11-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0007_auto_20191119_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default='00.00', max_digits=6, null=True, verbose_name='price'),
        ),
    ]
