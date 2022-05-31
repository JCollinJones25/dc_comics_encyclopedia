from ast import Delete
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Hero
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class HeroesList(TemplateView):
    template_name = 'heroes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heroes'] = Hero.objects.all()
        return context

class HeroCreate(CreateView):
    model = Hero
    fields = ['name', 'alter_ego', 'img', 'bio', 'powers', 'universe', 'affiliations', 'enemies']
    template_name = 'hero_create.html'
    def get_success_url(self):
        return reverse('hero_detail', kwargs={'pk': self.object.pk})

class HeroDetail(DetailView):
    model = Hero
    template_name = 'hero_detail.html'

class HeroUpdate(UpdateView):
    model = Hero
    fields = ['name', 'alter_ego', 'img', 'bio', 'powers', 'universe', 'affiliations', 'enemies']
    template_name = 'hero_update.html'
    def get_success_url(self):
        return reverse('hero_detail', kwargs={'pk': self.object.pk})

class HeroDelete(DeleteView):
    model = Hero
    template_name = 'hero_delete_confirmation.html'
    success_url = '/heroes/'

