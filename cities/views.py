from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City
from django.db.models import Q


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        return Exhibition.objects.filter(
            Q(name__icontains='최근') | Q(date__icontains='2023.07')
        )
