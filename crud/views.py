from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Language

class LanguageList(ListView):
    template_name = "crud/language/list.html"
    model = Language

class LanguageDetail(DetailView):
    template_name = "crud/language/detail.html"
    model = Language

class LanguageCreate(CreateView):
    template_name = "crud/language/create.html"
    model = Language

class LanguageUpdate(UpdateView):
    template_name = "crud/language/update.html"
    model = Language
    fields = ('language',)

class LanguageDelete(DeleteView):
    template_name = "crud/language/delete.html"
    model = Language