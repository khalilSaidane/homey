# Generated by Django 2.2.5 on 2020-01-20 13:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(upload_to=listings.models.upload_listing_image)),
                ('photo_1', models.ImageField(blank=True, upload_to=listings.models.upload_listing_image)),
                ('photo_2', models.ImageField(blank=True, upload_to=listings.models.upload_listing_image)),
                ('photo_3', models.ImageField(blank=True, upload_to=listings.models.upload_listing_image)),
                ('photo_4', models.ImageField(blank=True, upload_to=listings.models.upload_listing_image)),
                ('photo_5', models.ImageField(blank=True, upload_to=listings.models.upload_listing_image)),
                ('photo_6', models.ImageField(blank=True, upload_to=listings.models.upload_listing_image)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
