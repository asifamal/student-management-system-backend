# Generated by Django 5.0.6 on 2024-05-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studmanage', '0011_alter_student_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='previous_schooling',
            field=models.JSONField(default=list),
        ),
    ]