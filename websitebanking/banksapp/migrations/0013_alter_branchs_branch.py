# Generated by Django 3.2.18 on 2024-01-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0012_auto_20240109_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchs',
            name='branch',
            field=models.CharField(max_length=250),
        ),
    ]