# Generated by Django 2.2.6 on 2019-11-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0010_auction_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='admin',
            field=models.CharField(max_length=256),
        ),
    ]
