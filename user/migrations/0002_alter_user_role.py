# Generated by Django 4.0.1 on 2022-03-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('PLAYER', 'Player'), ('MANUFACTURER', 'Manufacturer'), ('CUSTOMER', 'Customer')], default='PLAYER', max_length=16),
        ),
    ]
