# Generated by Django 3.1.5 on 2021-03-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.FileField(blank=True, upload_to='product_images/'),
        ),
    ]
