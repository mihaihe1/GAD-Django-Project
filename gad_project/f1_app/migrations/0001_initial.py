# Generated by Django 2.2.5 on 2021-07-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('power_unit', models.CharField(max_length=30)),
                ('world_championships', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
