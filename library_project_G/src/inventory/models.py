from django.db import models
from library.models import Book 

class BookCondition(models.TextChoices):
    NEW = 'new', 'New'
    GOOD = 'good', 'Good'
    FAIR = 'fair', 'Fair'
    POOR = 'poor', 'Poor'

class Shelf(models.Model):
    """Model representing a shelf in the library"""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Shelf: {self.name} - Location: {self.location}"

class BookInventory(models.Model):
    """Model representing a physical copy of a book in the library inventory"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='inventory')
    condition = models.CharField(
        max_length=20,
        choices=BookCondition.choices,
        default=BookCondition.GOOD,
    )
    acquisition_date = models.DateField()
    retirement_date = models.DateField(null=True, blank=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name='books')
    retired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} ({self.condition})"
