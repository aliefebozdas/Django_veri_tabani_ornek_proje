# Generated by Django 4.2.7 on 2023-11-21 03:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]