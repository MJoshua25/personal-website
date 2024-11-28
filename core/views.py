from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, get_list_or_404
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        
        context['personal_info'] = get_object_or_404(models.PersonalInfo.objects.filter(statut=True))
        context['contact_info'] = get_object_or_404(models.ContactInfo.objects.filter(statut=True))
        context['projects'] = get_list_or_404(models.Project.objects.filter(status=True))
        return context
        