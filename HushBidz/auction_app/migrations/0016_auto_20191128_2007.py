# Generated by Django 2.2.6 on 2019-11-29 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0015_auto_20191126_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_image', verbose_name='image'),
        ),
    ]