
from django.conf.urls import url
from news.views import NewsEntryCreateView, NewsEntryUpdateView, NewsEntryListView, NewsEntryDetailView, \
    NewsBasePublishView, HistoryEntryCreateView, HistoryEntryDetailView

urlpatterns = [
    url(r'^$', NewsEntryListView.as_view(), name='news_list'),
    url(r'^new/$', NewsEntryCreateView.as_view(), name='news_create'),
    url(r'^(?P<pk>\d+)/$', NewsEntryDetailView.as_view(), name='news_detail'),
    url(r'^(?P<pk>\d+)/update/$', NewsEntryUpdateView.as_view(), name='news_update'),
    url(r'^(?P<pk>\d+)/publish/$', NewsBasePublishView.as_view(), name='news_publish'),
]