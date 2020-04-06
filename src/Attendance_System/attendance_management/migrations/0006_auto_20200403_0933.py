# Generated by Django 3.0.3 on 2020-04-03 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_management', '0005_courseoffered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseslots',
            name='timing_list',
        ),
        migrations.RemoveField(
            model_name='faculties',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='students',
            name='userId',
        ),
        migrations.DeleteModel(
            name='CourseOffered',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='CourseSlots',
        ),
        migrations.DeleteModel(
            name='Faculties',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='Timings',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]