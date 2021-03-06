# Generated by Django 4.0.2 on 2022-04-09 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0007_application_chosen_application_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='chosen',
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Make Decision Later'), ('a', 'Approve'), ('r', 'Reject')], default='p', max_length=50),
        ),
    ]
