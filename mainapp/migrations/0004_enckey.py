# Generated by Django 4.1.2 on 2023-05-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_enckey'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_key', models.CharField(max_length=6)),
            ],
        ),
    ]
