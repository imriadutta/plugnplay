# Generated by Django 4.2.1 on 2023-05-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_video_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.FileField(upload_to=''),
        ),
    ]
