# Generated by Django 3.1.2 on 2020-10-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.TextField(max_length=100)),
                ('username', models.TextField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True)),
                ('Age', models.IntegerField()),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('url', models.TextField(max_length=100)),
                ('imgposition', models.TextField(max_length=100)),
                ('author', models.TextField(max_length=100)),
                ('createdate', models.DateField(auto_now_add=True)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
