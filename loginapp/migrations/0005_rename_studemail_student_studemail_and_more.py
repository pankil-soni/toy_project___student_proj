# Generated by Django 4.2.4 on 2023-08-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_student_studemail_student_studpassword_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studemail',
            new_name='studEmail',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studpassword',
            new_name='studPassword',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studusername',
            new_name='studUsername',
        ),
        migrations.AddField(
            model_name='student',
            name='studBirthdate',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='studAge',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='studClass',
            field=models.IntegerField(default=None),
        ),
    ]