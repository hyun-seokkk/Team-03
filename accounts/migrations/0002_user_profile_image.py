# Generated by Django 3.2.18 on 2023-04-28 08:40

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=accounts.models.profile_img_path),
        ),
    ]