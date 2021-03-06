# Generated by Django 2.2.6 on 2019-11-19 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0006_auto_20191119_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, default='item description', max_length=256, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(default='An Item', max_length=256, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default='00.00', max_digits=6, null=True, verbose_name='proce'),
        ),
    ]
