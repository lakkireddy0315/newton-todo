# Generated by Django 3.2.7 on 2022-09-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=2),
        ),
    ]
