# Generated by Django 5.1.4 on 2024-12-23 21:32

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slig',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]