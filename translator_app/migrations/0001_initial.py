# Generated by Django 4.2.2 on 2023-09-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField()),
                ('output_text', models.TextField()),
                ('language_used', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
