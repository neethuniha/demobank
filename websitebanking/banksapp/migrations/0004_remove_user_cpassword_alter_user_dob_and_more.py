# Generated by Django 4.2.7 on 2023-12-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0003_user_delete_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpassword',
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='phnno',
            field=models.IntegerField(),
        ),
    ]
