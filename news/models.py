from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class NewsBase(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    publication_date = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User)

    class Meta:
        ordering = ["-publication_date"]

    def __str__(self):
        return self.title


class NewsEntry(NewsBase):
    def get_absolute_url(self):
        return reverse('news_detail', args=[self.pk])


class HistoryEntry(NewsBase):
    def get_absolute_url(self):
        return reverse('history_detail', args=[self.pk])


class HistoryPhoto(models.Model):
    history_entry = models.ForeignKey(HistoryEntry)

    photo = models.ImageField(upload_to="history_photos")
    description = models.TextField()



