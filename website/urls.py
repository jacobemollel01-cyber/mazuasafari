
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("about/", views.about, name="about"),
    path("safaris/", views.safaris, name="safaris"),
    path("destinations/", views.destinations, name="destinations"),
    path("packages/", views.packages, name="packages"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]

