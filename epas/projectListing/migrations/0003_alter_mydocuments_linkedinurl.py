# Generated by Django 4.0.2 on 2022-02-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0002_post_active_post_course_post_desirednumstudents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydocuments',
            name='linkedinURl',
            field=models.URLField(),
        ),
    ]