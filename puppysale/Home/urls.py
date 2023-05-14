from django.urls import path, include
from . import views
from .views import video
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home,name = "Home"),
    path("about/", views.about, name = "About"),
    path("contact/", views.contact, name = "Contact"),
    path("register/", views.register_request, name = "Register"),
    path("",video),
]

urlpatterns += staticfiles_urlpatterns()