# Generated by Django 3.2.18 on 2024-01-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0018_alter_branchs_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
