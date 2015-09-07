import django
from django.db import models


# Create your models here.
from django.utils import timezone
from companies.managers import BannerManager


class Banner(models.Model):
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners')
    link = models.URLField()

    start = models.DateField(default=timezone.now().date)
    end = models.DateField()

    objects = BannerManager()

    class Meta:
        ordering = ['?']