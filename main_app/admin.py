from django.contrib import admin
from .models import Hero, Villain, HeroTeam, VillainTeam

# Register your models here.

admin.site.register(Hero)
admin.site.register(Villain)
admin.site.register(HeroTeam)
admin.site.register(VillainTeam)