# Generated by Django 4.2.7 on 2023-11-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog", name="image", field=models.ImageField(upload_to="blogs"),
        ),
    ]
