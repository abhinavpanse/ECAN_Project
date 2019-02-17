# Generated by Django 2.1.7 on 2019-02-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='sales',
        ),
        migrations.AddField(
            model_name='customuser',
            name='sales',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
