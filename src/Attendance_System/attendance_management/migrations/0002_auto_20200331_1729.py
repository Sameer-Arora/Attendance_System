# Generated by Django 3.0.3 on 2020-03-31 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='userId',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='attendance_management.Users'),
        ),
    ]
