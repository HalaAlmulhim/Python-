# Generated by Django 3.2 on 2021-04-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_app', '0003_alter_show_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
