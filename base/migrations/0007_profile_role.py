# Generated by Django 4.0 on 2022-01-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'User'), (2, 'Supplier'), (3, 'Admin'), (4, 'SuperUser')], null=True),
        ),
    ]
