# Generated by Django 4.0 on 2022-01-10 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
