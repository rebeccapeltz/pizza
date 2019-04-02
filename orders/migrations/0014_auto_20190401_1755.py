# Generated by Django 2.1.7 on 2019-04-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190401_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='size',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='style',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='unitPrice',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='display',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
