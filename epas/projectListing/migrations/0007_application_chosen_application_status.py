# Generated by Django 4.0.2 on 2022-04-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0006_application_projectid'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='chosen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
