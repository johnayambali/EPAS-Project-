# Generated by Django 4.0.2 on 2022-04-25 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0015_remove_post_relatedprogram_alter_post_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='relatedProgram',
            field=models.CharField(blank=True, default='null', max_length=100, verbose_name='Program:'),
        ),
    ]
