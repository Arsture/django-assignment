# Generated by Django 5.0.2 on 2024-02-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_alter_tag_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]