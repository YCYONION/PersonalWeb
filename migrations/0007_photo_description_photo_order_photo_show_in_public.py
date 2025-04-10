# Generated by Django 5.1 on 2025-03-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_photo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='show_in_public',
            field=models.BooleanField(default=True),
        ),
    ]
