# Generated by Django 4.2.5 on 2023-12-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_album_viewer', '0005_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='album_covers/'),
        ),
    ]
