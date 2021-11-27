# Generated by Django 3.2.9 on 2021-11-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_delete_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
    ]