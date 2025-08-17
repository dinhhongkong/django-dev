from django.urls import path

from apps.film import views

urlpatterns = [
    path("get-all-films/", views.FilmListView.as_view())
]