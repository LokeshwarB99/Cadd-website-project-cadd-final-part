# Generated by Django 4.2.1 on 2023-06-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0023_coursegroup_core_coursegroupid_module_coursegroupid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='cores',
            field=models.ManyToManyField(null=True, related_name='contains', to='caddWebsiteMain.core'),
        ),
    ]
