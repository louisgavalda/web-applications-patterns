from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Markdown content
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="notes")

    def __str__(self):
        return self.title
