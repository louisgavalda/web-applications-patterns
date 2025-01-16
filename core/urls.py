from django.urls import path
from .api import api

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("notes", views.notes_list_partial, name="notes_list_partial"),
    path("note/new/", views.note_create, name="note_create"),
    path("note/<int:note_id>/", views.note_detail, name="note_detail"),
    path("note/<int:note_id>/edit/", views.note_edit, name="note_edit"),
    path("note/<int:note_id>/delete/", views.note_delete, name="note_delete"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tag/new/", views.tag_create, name="tag_create"),
    path("tag/<int:tag_id>/delete/", views.tag_delete, name="tag_delete"),
    path("tag/<str:tag_name>/", views.tag_notes, name="tag_notes"),
    path("api/", api.urls),
]
