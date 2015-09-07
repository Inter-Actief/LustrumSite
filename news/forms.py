from django.forms import ModelForm, inlineformset_factory
from news.models import HistoryEntry, HistoryPhoto

HistoryPhotoFormset = inlineformset_factory(HistoryEntry, HistoryPhoto, fields=['photo', 'description'], extra=1)