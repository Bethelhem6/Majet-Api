# Generated by Django 5.1.4 on 2024-12-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_rename_category_id_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
