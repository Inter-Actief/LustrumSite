# Create your views here.
from django.views.generic import TemplateView
from companies.models import Banner
from news.models import NewsEntry, HistoryEntry


class FrontpageView(TemplateView):
    template_name = "frontpage.html"

    def get_context_data(self, **kwargs):
        context = super(FrontpageView, self).get_context_data(**kwargs)

        news_items = NewsEntry.objects.filter(publication_date__isnull=False)

        context["news_headline"] = news_items[0] if news_items else None
        context["news_items"] = news_items[1:4] if len(news_items) > 1 else []

        context["historyentry"] = HistoryEntry.objects.filter(publication_date__isnull=False).first()
        context["historyentry_photos"] = context["historyentry"].historyphoto_set.all()[0:1] if context["historyentry"] else None

        context["banner_list"] = Banner.objects.filter_visible()[0:5]

        return context
