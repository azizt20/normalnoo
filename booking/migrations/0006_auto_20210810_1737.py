# Generated by Django 3.1.7 on 2021-08-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20210810_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_waiting',
            name='order_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]