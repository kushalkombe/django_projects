# Generated by Django 2.2.2 on 2020-01-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]
