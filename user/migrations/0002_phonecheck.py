# Generated by Django 3.1.2 on 2020-11-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'phonechecks',
            },
        ),
    ]
