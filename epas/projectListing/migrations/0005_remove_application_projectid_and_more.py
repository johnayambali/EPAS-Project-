# Generated by Django 4.0.2 on 2022-04-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0004_application_projectid_alter_post_isapproved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='projectID',
        ),
        migrations.AlterField(
            model_name='application',
            name='appDetails',
            field=models.TextField(),
        ),
    ]
