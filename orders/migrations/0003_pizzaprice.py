# Generated by Django 2.1.7 on 2019-03-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190329_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
                ('style', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=7)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
