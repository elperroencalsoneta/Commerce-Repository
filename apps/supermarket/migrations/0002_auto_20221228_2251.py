# Generated by Django 3.1.7 on 2022-12-28 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supermarket',
            old_name='location',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='supermarket',
            old_name='open_hours',
            new_name='operating_hours',
        ),
        migrations.RenameField(
            model_name='supermarket',
            old_name='image',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='supermarket',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='supermarket',
            name='distance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='supermarket',
            name='open_state',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='website',
            field=models.URLField(max_length=255),
        ),
    ]