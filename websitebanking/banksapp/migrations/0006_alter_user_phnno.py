# Generated by Django 4.2.7 on 2023-12-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0005_alter_user_phnno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phnno',
            field=models.IntegerField(),
        ),
    ]
