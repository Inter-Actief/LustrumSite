from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, ListView
from companies.models import Banner
from tools.mixins import SuperuserRequiredMixin


class BannerCreateView(SuperuserRequiredMixin, CreateView):
    model = Banner
    fields = "__all__"

    success_url = reverse_lazy('banner_list')

class BannerUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Banner
    fields = "__all__"

    success_url = reverse_lazy('banner_list')


class BannerListView(SuperuserRequiredMixin, ListView):
    model = Banner
    ordering = ['start']

    def get_context_data(self, **kwargs):
        context = super(BannerListView, self).get_context_data(**kwargs)

        context["now"] = timezone.now().date

        return context
