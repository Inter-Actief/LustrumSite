from django.conf.urls import url

from news.views import HistoryEntryUpdateView, HistoryEntryListView, HistoryEntryCreateView, HistoryEntryDetailView, \
    NewsBasePublishView

urlpatterns = [
    url(r'^$', HistoryEntryListView.as_view(), name='history_list'),
    url(r'^new/$', HistoryEntryCreateView.as_view(), name='history_create'),
    url(r'^(?P<pk>\d+)/$', HistoryEntryDetailView.as_view(), name='history_detail'),
    url(r'^(?P<pk>\d+)/update/$', HistoryEntryUpdateView.as_view(), name='history_update'),
    url(r'^(?P<pk>\d+)/publish/$', NewsBasePublishView.as_view(), name='history_publish')
]