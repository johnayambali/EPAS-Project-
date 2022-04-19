# Generated by Django 4.0.2 on 2022-04-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectListing', '0009_rename_status_application_applicationstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='assigned',
            field=models.BooleanField(default=False, verbose_name='Approve?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='appDetails',
            field=models.TextField(verbose_name="Tell us why you'd like this project"),
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.CharField(default='null', max_length=100, verbose_name='Course:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='Project description:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='desiredNumStudents',
            field=models.IntegerField(verbose_name='Ideal number of students'),
        ),
        migrations.AlterField(
            model_name='post',
            name='isApproved',
            field=models.BooleanField(default=False, verbose_name='Approve?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='maxNumStudents',
            field=models.IntegerField(verbose_name='Max number of students:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='maxTermLength',
            field=models.IntegerField(verbose_name='Max number of months:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='minTermLength',
            field=models.IntegerField(verbose_name='Min number of months:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='relatedProgram',
            field=models.CharField(max_length=100, verbose_name='Program:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Project name:'),
        ),
    ]