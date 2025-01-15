from typing import List

from ninja import NinjaAPI, ModelSchema, Schema

from .models import Note


api = NinjaAPI()


class NoteSchema(ModelSchema):
    class Meta:
        model = Note
        fields = ["title", "content", "tags"]


# class NoteOutSchema(Schema):
#     id: int
#     title: str
#     content: str
#     tags: List[str]


@api.get("/notes/", response=list[NoteSchema])
def list_notes(request):
    # List with possible filters (tags, full-text search)
    notes = Note.objects.all()
    return notes


@api.post("/notes/")
def create_note(request, payload: NoteSchema):
    # Creation with tag management
    pass


@api.get("/notes/{note_id}")
def get_note(request, note_id: int):
    # Details of a note with its tags
    pass


@api.put("/notes/{note_id}")
def update_note(request, note_id: int, payload: NoteSchema):
    # Update with tag management
    pass


@api.delete("/notes/{note_id}")
def delete_note(request, note_id: int):
    # Deletion
    pass


@api.get("/tags/")
def list_tags(request):
    # List of tags with note count
    pass
