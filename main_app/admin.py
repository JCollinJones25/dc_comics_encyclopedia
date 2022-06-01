from django.contrib import admin
from .models import Hero, Villain, Comic

# Register your models here.

admin.site.register(Hero)
admin.site.register(Villain)
admin.site.register(Comic)