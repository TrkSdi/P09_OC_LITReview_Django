from pathlib import Path
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


NOTE= (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),)

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/images/", blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    @property    
    def is_reviewed(self):
        countreview = Review.objects.filter(ticket=self).count()
        return bool(countreview)
    
    def __str__(self):
        return f"{self.title}"
    
class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.CharField(max_length=5, choices=NOTE, blank=False, default=None)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.headline}"
    
    @property
    def star_display(self):
        if self.rating == "5":
            url =  Path("/src/media/star-rating/5star.png")
            return url
        elif self.rating == "4":
            url =  Path("/src/media/star-rating/4star.png")
            return url
        elif self.rating == "3":
            url =  Path("/src/media/star-rating/3star.png")
            return url
        elif self.rating == "2":
            url =  Path("/src/media/star-rating/2star.png")
            return url
        elif self.rating == "1":
            url =  Path("/src/media/star-rating/1star.png")
            return url
        else:
            url =  Path("/src/media/star-rating/0star.png")
            return url

