# Generated by Django 4.2.1 on 2023-07-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0039_caddbasicdetails_youtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('banner', models.ImageField(upload_to='advertisements/')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
