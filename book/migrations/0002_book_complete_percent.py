# Generated by Django 3.1.2 on 2020-11-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='complete_percent',
            field=models.IntegerField(default=0),
        ),
    ]
