# Generated by Django 2.1.3 on 2019-04-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20190403_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='产品列表',
            name='描述',
            field=models.TextField(blank=True),
        ),
    ]
