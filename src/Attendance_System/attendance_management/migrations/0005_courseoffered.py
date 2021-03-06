# Generated by Django 3.0.3 on 2020-04-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_management', '0004_auto_20200331_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOffered',
            fields=[
                ('course_offered_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_year', models.CharField(max_length=4)),
                ('course_sem', models.BooleanField()),
                ('courseId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance_management.Courses')),
                ('course_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='attendance_management.Timings')),
                ('facId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance_management.Faculties')),
            ],
        ),
    ]
