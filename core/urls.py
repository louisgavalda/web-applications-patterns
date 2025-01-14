from django.urls import path
from .api import api

from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/", api.urls),
]
