# Generated by Django 4.2.1 on 2023-06-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0016_subcourseindex_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseGroupName', models.CharField(max_length=255)),
            ],
        ),
    ]
