# Generated by Django 3.2.18 on 2024-01-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksapp', '0014_user1_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materials', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='user1',
            name='district',
            field=models.CharField(choices=[('Idukki', 'Idukki'), ('Eranakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Kottayam', 'Kottayam')], max_length=250, null=True),
        ),
        migrations.RemoveField(
            model_name='user1',
            name='materials',
        ),
        migrations.AddField(
            model_name='user1',
            name='materials',
            field=models.ManyToManyField(to='banksapp.Materials'),
        ),
    ]
