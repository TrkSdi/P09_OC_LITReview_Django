from django.db import models
from django.contrib.auth.models import User

NOTE= (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),)

class Review(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=5, choices=NOTE)
    comment = models.CharField(max_length=500)
    
class BookToReview(models.Model):
    book_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    review_title = models.CharField(max_length=100)
    note = models.CharField(max_length=5, choices=NOTE, blank=False, default=None)
    comment = models.CharField(max_length=500)

class TicketToReview(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=5, choices=NOTE, blank=False, default=None)
    comment = models.CharField(max_length=500)
    
class TicketCreation(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    

