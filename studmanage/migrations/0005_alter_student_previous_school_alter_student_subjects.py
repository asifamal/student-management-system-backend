# Generated by Django 5.0.6 on 2024-05-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studmanage', '0004_alter_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='previous_school',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.TextField(),
        ),
    ]