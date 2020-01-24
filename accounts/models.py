from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing


def upload_profile_image(instance, filename):
    return "profile/{user}/{filename}".format(user=instance.user, filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_profile_image, blank=True, default='profile/default.jpeg')
    favorite_properties = models.ManyToManyField(Listing, blank=True, related_name='favorite_properties')
