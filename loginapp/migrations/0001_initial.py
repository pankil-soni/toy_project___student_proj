# Generated by Django 4.2.4 on 2023-08-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studName', models.TextField(max_length=20)),
                ('studAge', models.IntegerField()),
                ('studAddress', models.TextField(max_length=50)),
                ('studClass', models.IntegerField()),
            ],
        ),
    ]
