from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name='about'),
    path('heroes/', views.HeroesList.as_view(), name='heroes_list'),
    path('heroes/new/', views.HeroCreate.as_view(), name='hero_create'),
    path('heroes/<int:pk>', views.HeroDetail.as_view(), name='hero_detail'),
    path('heroes/<int:pk>/update', views.HeroUpdate.as_view(), name='hero_update'),
    path('heroes/<int:pk>/delete', views.HeroDelete.as_view(), name='hero_delete'),
    path('villains/', views.VillainsList.as_view(), name='villains_list'),
    path('villains/<int:pk>', views.VillainDetail.as_view(), name='villain_detail'),
    path('villains/new/', views.VillainCreate.as_view(), name='villain_create'),
    path('villain/<int:pk>/update', views.VillainUpdate.as_view(), name='villain_update'),
    path('villain/<int:pk>/delete', views.VillainDelete.as_view(), name='villain_delete'),
    path('heroteams/new', views.HeroTeamCreate.as_view(), name='heroteam_create'),
    path('heroteams/<int:pk>', views.HeroTeamDetail.as_view(), name='heroteam_detail'),
    path('heroteams/<int:pk>/update', views.HeroTeamUpdate.as_view(), name='heroteam_update'),
    path('heroteams/<int:pk>/delete', views.HeroTeamDelete.as_view(), name='heroteam_delete'),
]
