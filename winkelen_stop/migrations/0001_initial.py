# Generated by Django 4.1 on 2022-10-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('pwd', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('nationality', models.CharField(max_length=150)),
            ],
        ),
    ]
