# Generated by Django 4.2.4 on 2023-10-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0003_remove_modelcategory_title_modelcategory_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="physicsmodels",
            name="title",
            field=models.CharField(default="Physics Model", max_length=150),
        ),
    ]
