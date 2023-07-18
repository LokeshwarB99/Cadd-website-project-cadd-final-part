# Generated by Django 4.2.1 on 2023-06-19 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0014_remove_coursecontenttitle_courseid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='courseContentTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentTitle', models.CharField(max_length=100)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.courseindex')),
            ],
        ),
        migrations.CreateModel(
            name='courseContentDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentDescription', models.TextField()),
                ('courseContentTitleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.coursecontenttitle')),
            ],
        ),
    ]