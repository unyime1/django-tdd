# Generated by Django 3.2.4 on 2021-06-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='name',
            field=models.CharField(max_length=700, unique=True),
        ),
    ]
