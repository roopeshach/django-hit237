# Generated by Django 4.2 on 2023-05-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Waste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRecovery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('process', models.TextField()),
            ],
        ),
    ]
