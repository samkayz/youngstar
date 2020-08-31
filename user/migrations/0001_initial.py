# Generated by Django 3.1 on 2020-08-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questn', models.TextField(blank=True, null=True)),
                ('option1', models.TextField(blank=True, null=True)),
                ('option2', models.TextField(blank=True, null=True)),
                ('option4', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
