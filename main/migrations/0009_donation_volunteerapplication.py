# Generated by Django 4.2.7 on 2023-12-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_order_animals_order_animals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_card_number', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('reasons_for_volunteering', models.TextField()),
                ('skills', models.TextField()),
            ],
        ),
    ]
