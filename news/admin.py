from django.contrib import admin
from news.models import NewsEntry, HistoryEntry

admin.site.register(NewsEntry)
admin.site.register(HistoryEntry)
