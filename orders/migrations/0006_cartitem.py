# Generated by Django 2.1.7 on 2019-03-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190331_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('size', models.IntegerField()),
                ('style', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=10)),
                ('toppings', models.CharField(max_length=50)),
                ('unitPrice', models.IntegerField()),
            ],
        ),
    ]
