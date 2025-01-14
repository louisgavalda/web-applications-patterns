from django.db import models


from django.db import models


class Book(models.Model):
    STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("BORROWED", "Borrowed"),
        ("MAINTENANCE", "Maintenance"),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="AVAILABLE"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    # TODO: The method is_available() should True if (and only if) the book is available.
    def is_available(self):
        pass


class Borrower(models.Model):
    # TODO: Add the following fields: name, email, age (make it optional).
    pass


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    # TODO: The method is_overdue() shoud return True if (and only if) the book should have already been returned (i.e. late loan).
    def is_overdue(self):
        pass
