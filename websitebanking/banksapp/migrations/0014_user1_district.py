# Generated by Django 3.2.18 on 2024-01-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0013_alter_branchs_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='district',
            field=models.CharField(max_length=250, null=True),
        ),
    ]