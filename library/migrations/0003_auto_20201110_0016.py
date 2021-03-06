# Generated by Django 3.1.2 on 2020-11-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201106_2247'),
        ('library', '0002_shelf_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='index',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='shelf',
            unique_together={('user', 'index')},
        ),
    ]
