# Generated by Django 4.2.1 on 2023-06-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0020_moduledescription_coredescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='corename',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='module',
            name='modulename',
            field=models.CharField(max_length=100),
        ),
    ]
