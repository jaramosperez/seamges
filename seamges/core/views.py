from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request):
        return render(request, self.template_name, {'title':"Sistema Experto de Apoyo al Monitoreo GES SEAMGES"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

