# Generated by Django 4.0.2 on 2022-04-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0012_alter_application_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='isApproved',
            field=models.BooleanField(default=False, verbose_name='Approve?'),
        ),
    ]
