# Generated by Django 3.2.4 on 2021-10-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
