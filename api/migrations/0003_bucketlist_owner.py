# Generated by Django 3.2.4 on 2021-06-13 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_bucketlist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bucketlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
