# Generated by Django 3.1.7 on 2022-12-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0002_auto_20221228_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supermarket',
            name='open_state',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='operating_hours',
            field=models.TextField(max_length=200),
        ),
    ]