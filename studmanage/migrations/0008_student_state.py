# Generated by Django 5.0.6 on 2024-05-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studmanage', '0007_remove_city_state_alter_student_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='state',
            field=models.CharField(default='default', max_length=200),
        ),
    ]