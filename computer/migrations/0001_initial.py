# Generated by Django 3.2.7 on 2021-09-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('RAM_size', models.IntegerField()),
                ('CPU_frequency', models.IntegerField()),
                ('monitor', models.IntegerField()),
            ],
            options={
                'db_table': 'computers',
            },
        ),
    ]
