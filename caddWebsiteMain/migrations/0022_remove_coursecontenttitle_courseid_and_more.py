# Generated by Django 4.2.1 on 2023-06-24 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0021_alter_core_corename_alter_module_modulename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontenttitle',
            name='courseId',
        ),
        migrations.RemoveField(
            model_name='courseindex',
            name='courseGroupId',
        ),
        migrations.RemoveField(
            model_name='coursewithsubcourse',
            name='courseId',
        ),
        migrations.RemoveField(
            model_name='coursewithsubcourse',
            name='subCourseId',
        ),
        migrations.RemoveField(
            model_name='subcoursecontentdescription',
            name='subCourseContentTitleId',
        ),
        migrations.RemoveField(
            model_name='subcoursecontenttitle',
            name='subCourseId',
        ),
        migrations.DeleteModel(
            name='courseContentDescription',
        ),
        migrations.DeleteModel(
            name='courseContentTitle',
        ),
        migrations.DeleteModel(
            name='CourseGroup',
        ),
        migrations.DeleteModel(
            name='courseIndex',
        ),
        migrations.DeleteModel(
            name='CourseWithSubCourse',
        ),
        migrations.DeleteModel(
            name='SubCourseContentDescription',
        ),
        migrations.DeleteModel(
            name='SubCourseContentTitle',
        ),
        migrations.DeleteModel(
            name='SubCourseIndex',
        ),
    ]
