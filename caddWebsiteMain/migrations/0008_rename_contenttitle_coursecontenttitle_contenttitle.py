# Generated by Django 4.2.1 on 2023-06-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0007_coursecontentdescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecontenttitle',
            old_name='ContentTitle',
            new_name='contentTitle',
        ),
    ]
