from django.conf.urls import url
from companies.views import BannerListView, BannerCreateView, BannerUpdateView

urlpatterns = [
    url(r'^$', BannerListView.as_view(), name="banner_list"),
    url(r'^new/$', BannerCreateView.as_view(), name="banner_create"),
    url(r'^(?P<pk>\d+)/update/$', BannerUpdateView.as_view(), name="banner_update")
]