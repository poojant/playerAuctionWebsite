# Generated by Django 2.1 on 2018-08-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_team1'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
