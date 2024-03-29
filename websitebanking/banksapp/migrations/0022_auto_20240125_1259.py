# Generated by Django 3.2.18 on 2024-01-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0021_alter_materials_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='materials',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user1',
            name='ac_type',
            field=models.CharField(choices=[('S', 'Savings Account'), ('C', 'Current Account')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='branch',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='district',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='email',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user1',
            name='phnno',
            field=models.IntegerField(null=True),
        ),
    ]
