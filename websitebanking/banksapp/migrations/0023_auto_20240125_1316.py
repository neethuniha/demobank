# Generated by Django 3.2.18 on 2024-01-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0022_auto_20240125_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='materials',
        ),
        migrations.AddField(
            model_name='user1',
            name='materials',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
