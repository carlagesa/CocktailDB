# Generated by Django 5.1 on 2024-08-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('glass_type', models.CharField(max_length=100)),
                ('alcoholic', models.BooleanField(default=True)),
                ('instructions', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('ingredients', models.ManyToManyField(related_name='cocktails', to='cocktails.ingredient')),
            ],
        ),
    ]
