# Generated by Django 4.2.7 on 2023-12-11 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_animal_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
