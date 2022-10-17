# Generated by Django 4.1 on 2022-10-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('msg', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'feedback_webpage',
            },
        ),
    ]
