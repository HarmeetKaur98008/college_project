# Generated by Django 4.2.4 on 2023-09-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('prn', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=30)),
                ('sa', models.FileField(upload_to='')),
            ],
        ),
    ]
