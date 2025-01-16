from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Note, Tag


def home(request):
    notes = Note.objects.all().order_by("-updated_at")
    tags = Tag.objects.all()

    query = request.GET.get("q")
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    return render(
        request, "core/home.html", {"notes": notes, "tags": tags, "query": query}
    )


def notes_list_partial(request):
    search = request.GET.get("search", "")
    notes = Note.objects.filter(
        Q(title__icontains=search) | Q(content__icontains=search)
    )
    return render(request, "core/partials/notes_list.html", {"notes": notes})


def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "core/detail.html", {"note": note})


def note_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        tag_names = request.POST.getlist("tags")

        if title and content:
            note = Note.objects.create(title=title, content=content)

            # Gestion des tags
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
                note.tags.add(tag)

            return redirect("note_detail", note_id=note.id)

    tags = Tag.objects.all()
    return render(request, "core/create.html", {"tags": tags})


def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        tag_names = request.POST.getlist("tags")

        if title and content:
            note.title = title
            note.content = content
            note.save()

            # Tags update.
            note.tags.clear()
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
                note.tags.add(tag)

            return redirect("note_detail", note_id=note.id)

    tags = Tag.objects.all()
    return render(request, "core/create.html", {"note": note, "tags": tags})


def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note.delete()
        return redirect("home")

    return render(request, "core/delete.html", {"note": note})


def tag_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            # We use get_or_create so a tag won't be created twice.
            tag, created = Tag.objects.get_or_create(name=name.strip())
            if created:
                return redirect("tag_list")
            else:
                return render(
                    request,
                    "core/tag_create.html",
                    {"error": "This tag already exists."},
                )
    return render(request, "core/tag_create.html")


def tag_list(request):
    tags = Tag.objects.all().order_by("name")
    return render(request, "core/tag_list.html", {"tags": tags})


def tag_delete(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == "POST":
        # Delete the tag and redirect to another page.
        pass
    return render(request, "core/tag_delete.html", {"tag": tag})


def tag_notes(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    notes = Note.objects.filter(tags=tag).order_by("-updated_at")

    return render(request, "core/tag_notes.html", {"tag": tag, "notes": notes})
