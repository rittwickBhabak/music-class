# Generated by Django 3.2.7 on 2021-09-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='url',
        ),
        migrations.AddField(
            model_name='song',
            name='youTubeVideoID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
