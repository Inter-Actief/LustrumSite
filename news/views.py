from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone

from django.views.generic import CreateView, UpdateView, ListView, DetailView

from news.forms import HistoryPhotoFormset
from news.models import NewsEntry, HistoryEntry, NewsBase
from tools.mixins import SuperuserRequiredMixin


# Some classes can be omitted here, but to not scatter view code into my urls I decided to define them anyway
# Creation of news/history entries
class NewsBaseCreateView(SuperuserRequiredMixin, CreateView):
    fields = ['title', 'content']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        return super(NewsBaseCreateView, self).form_valid(form)


class NewsEntryCreateView(NewsBaseCreateView):
    model = NewsEntry


# Adapted from http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/
class HistoryEntryCreateView(SuperuserRequiredMixin, CreateView):
    model = HistoryEntry
    fields = ['title', 'content']

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        history_photo_form = HistoryPhotoFormset()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  history_photo_form = history_photo_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print(self.request)
        history_photo_form = HistoryPhotoFormset(self.request.POST, self.request.FILES)
        if form.is_valid() and history_photo_form.is_valid():
            return self.form_valid(form, history_photo_form)
        else:
            return self.form_invalid(form, history_photo_form)

    def form_valid(self, form, history_photo_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        history_photo_form.instance = self.object
        history_photo_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, history_photo_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  history_photo_form=history_photo_form))


# Update of news/histoty entries
class NewsBaseUpdateView(SuperuserRequiredMixin, UpdateView):
    fields = ['title', 'content']


class NewsEntryUpdateView(NewsBaseUpdateView):
    model = NewsEntry


# Adapted from http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/
class HistoryEntryUpdateView(SuperuserRequiredMixin, CreateView):
    model = HistoryEntry
    fields = ['title', 'content']

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        history_photo_form = HistoryPhotoFormset(instance=self.get_object())
        return self.render_to_response(
            self.get_context_data(form=form,
                                  history_photo_form = history_photo_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        history_photo_form = HistoryPhotoFormset(self.request.POST, self.request.FILES, instance=self.get_object())
        if form.is_valid() and history_photo_form.is_valid():
            return self.form_valid(form, history_photo_form)
        else:
            return self.form_invalid(form, history_photo_form)

    def form_valid(self, form, history_photo_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        history_photo_form.instance = self.object
        history_photo_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, history_photo_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  history_photo_form=history_photo_form))

# List of news/history entries
class NewsBaseListView(ListView):
    pass


class NewsEntryListView(NewsBaseListView):
    model = NewsEntry


class HistoryEntryListView(NewsBaseListView):
    model = HistoryEntry


# Detail of news/history entries
class NewsBaseDetailView(DetailView):
    def get_object(self, **kwargs):
        if self.request.user and self.request.user.is_superuser:
            queryset = self.get_queryset()
        else:
            queryset = self.get_queryset().filter(publication_date__isnull=False)

        return super(NewsBaseDetailView, self).get_object(queryset)


class NewsEntryDetailView(NewsBaseDetailView):
    model = NewsEntry


class HistoryEntryDetailView(NewsBaseDetailView):
    model = HistoryEntry


# Publish news/history entry
class NewsBasePublishView(DetailView):
    model = NewsBase
    template_name_suffix = '_publish_confirm'
    success_url = reverse_lazy('frontpage')

    def post(self, *args, **kwargs):
        obj = self.get_object()
        obj.publication_date = timezone.now()
        obj.save()

        messages.success(self.request, "Nieuwsbericht \"{0} \" is gepubliceerd!".format(obj.title))

        return HttpResponseRedirect(self.success_url)