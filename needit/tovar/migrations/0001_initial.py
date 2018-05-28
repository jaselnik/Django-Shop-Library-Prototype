# Generated by Django 2.0.1 on 2018-02-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=120)),
                ('post', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, help_text='300x240px', upload_to='images/', verbose_name='Ссылка картинки')),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]