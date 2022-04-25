# Generated by Django 4.0.2 on 2022-04-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0014_post_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='relatedProgram',
        ),
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.CharField(blank=True, choices=[('CSI4900', 'CSI4900')], default='null', max_length=100, verbose_name='Course:'),
        ),
    ]
