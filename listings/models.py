from django.db import models
from datetime import datetime
from django.conf import settings


def upload_listing_image(instance, filename):
    return "listing/{publisher}/{filename}".format(publisher=instance.publisher, filename=filename)


class Listing(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    # Optional field
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to=upload_listing_image)
    photo_1 = models.ImageField(upload_to=upload_listing_image, blank=True)
    photo_2 = models.ImageField(upload_to=upload_listing_image, blank=True)
    photo_3 = models.ImageField(upload_to=upload_listing_image, blank=True)
    photo_4 = models.ImageField(upload_to=upload_listing_image, blank=True)
    photo_5 = models.ImageField(upload_to=upload_listing_image, blank=True)
    photo_6 = models.ImageField(upload_to=upload_listing_image, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title
