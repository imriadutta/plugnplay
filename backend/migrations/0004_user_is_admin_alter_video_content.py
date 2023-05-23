# Generated by Django 4.2.1 on 2023-05-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_video_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.FileField(upload_to='media/'),
        ),
    ]
