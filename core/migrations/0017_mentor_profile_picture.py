# Generated by Django 5.0 on 2024-06-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_delete_timeblock_alter_mentor_time_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
