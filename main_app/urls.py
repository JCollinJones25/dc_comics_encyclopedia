from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name='about'),
    path('heroes/', views.HeroesList.as_view(), name='heroes_list'),
    path('heroes/<int:pk>', views.HeroDetail.as_view(), name='hero_detail')
]
