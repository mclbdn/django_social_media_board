# Generated by Django 3.2.8 on 2021-10-26 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_board', '0002_post_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
