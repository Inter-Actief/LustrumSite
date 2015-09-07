from django.db import models
from django.utils import timezone


class BannerManager(models.Manager):
    def filter_visible(self):
        return self.filter(start__lte=timezone.now(), end__gt=timezone.now())