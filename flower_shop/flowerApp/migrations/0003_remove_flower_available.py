# Generated by Django 4.1.7 on 2023-03-22 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowerApp', '0002_flower_name_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='available',
        ),
    ]
