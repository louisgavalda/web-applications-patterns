from datetime import datetime
from typing import List

from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from .models import Note, Tag

api = NinjaAPI()


# Below are the schemas used by Django Ninja.


class TagSchema(Schema):
    id: int
    name: str


class TagCreateSchema(Schema):
    name: str


class NoteSchema(Schema):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    tags: List[TagSchema]


class NoteCreateSchema(Schema):
    title: str
    content: str
    tags: list[str] | None = []  # Never do this in Python!.. Do you know why?


class NoteUpdateSchema(Schema):
    title: str | None
    content: str | None
    tags: list[str] | None


class ErrorSchema(Schema):
    message: str


# Below are the definitions of the endpoints of our API.


@api.get("/notes/", response=List[NoteSchema])
def list_notes(request, search: str | None = None, tag: str | None = None):
    queryset = Note.objects.all()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(
                content__icontains=search
            )  # Concise way for specifying complex conditions using the Django ORM.
        )

    if tag:
        queryset = queryset.filter(tags__name=tag)

    return queryset.order_by("-updated_at")


@api.get("/notes/{note_id}", response=NoteSchema)
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note


@api.post("/notes/", response={201: NoteSchema, 400: ErrorSchema})
def create_note(request, payload: NoteCreateSchema):
    try:
        note = Note.objects.create(title=payload.title, content=payload.content)

        # Gestion des tags
        for tag_name in payload.tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
            note.tags.add(tag)

        return 201, note
    except Exception as e:
        return 400, {"message": str(e)}


@api.put("/notes/{note_id}", response={200: NoteSchema, 400: ErrorSchema})
def update_note(request, note_id: int, payload: NoteUpdateSchema):
    note = get_object_or_404(Note, id=note_id)

    try:
        if payload.title is not None:
            note.title = payload.title
        if payload.content is not None:
            note.content = payload.content

        note.save()

        # We update the tags of the note if some were specified.
        if payload.tags is not None:
            note.tags.clear()
            for tag_name in payload.tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
                note.tags.add(tag)

        return 200, note
    except Exception as e:
        return 400, {"message": str(e)}


@api.delete("/notes/{note_id}", response={204: None, 404: ErrorSchema})
def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return 204, None


# Endpoints Tags
@api.get("/tags/", response=List[TagSchema])
def list_tags(request):
    return Tag.objects.all().order_by("name")


@api.post("/tags/", response={201: TagSchema, 400: ErrorSchema})
def create_tag(request, payload: TagCreateSchema):
    try:
        tag, created = Tag.objects.get_or_create(name=payload.name.strip())
        status = 201 if created else 400
        return status, tag if created else {"message": "Tag already exists"}
    except Exception as e:
        return 400, {"message": str(e)}


@api.delete("/tags/{tag_id}", response={204: None, 404: ErrorSchema})
def delete_tag(request, tag_id: int):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return 204, None
