# Generated by Django 4.2.1 on 2023-06-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0017_coursegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseindex',
            name='courseGroupId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='caddWebsiteMain.coursegroup'),
        ),
    ]
