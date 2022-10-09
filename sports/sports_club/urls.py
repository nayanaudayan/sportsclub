from django.urls import path
from .import views

urlpatterns=[
    path('home',views.sports_home),
    path('about',views.sports_about),
    path('games',views.sports_games),
    path('subscription',views.sports_subscription),
    path('contact',views.sports_contact)
]