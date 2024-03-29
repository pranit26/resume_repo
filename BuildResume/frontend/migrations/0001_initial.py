# Generated by Django 4.2.9 on 2024-01-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('contact_number', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('tech_skills', models.CharField(max_length=250)),
                ('experience', models.IntegerField()),
            ],
            options={
                'db_table': 'candidates',
                'managed': False,
            },
        ),
    ]
