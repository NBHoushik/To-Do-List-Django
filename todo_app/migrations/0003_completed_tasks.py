# Generated by Django 5.2.3 on 2025-07-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_user_data_user_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='completed_tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField()),
            ],
        ),
    ]
