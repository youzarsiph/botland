# Generated by Django 5.1 on 2024-08-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(db_index=True, help_text='Message content'),
        ),
    ]
