# Generated by Django 4.1.1 on 2022-09-27 09:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_alter_stories_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
