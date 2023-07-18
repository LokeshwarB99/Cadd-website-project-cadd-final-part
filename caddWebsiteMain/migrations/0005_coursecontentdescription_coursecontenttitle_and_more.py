# Generated by Django 4.2.1 on 2023-06-07 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0004_aboutus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseContentDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='courseContentTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContentTitle', models.CharField(max_length=100)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.courseindex')),
            ],
        ),
        migrations.CreateModel(
            name='subCourseContentDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='subCourseContentTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentTitle', models.CharField(max_length=100)),
                ('subCourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.subcourseindex')),
            ],
        ),
        migrations.RemoveField(
            model_name='subcoursedescription',
            name='subCourseId',
        ),
        migrations.DeleteModel(
            name='courseDescription',
        ),
        migrations.DeleteModel(
            name='subCourseDescription',
        ),
        migrations.AddField(
            model_name='subcoursecontentdescription',
            name='subCourseContentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.subcoursecontenttitle'),
        ),
        migrations.AddField(
            model_name='coursecontentdescription',
            name='courseContentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.coursecontenttitle'),
        ),
    ]
