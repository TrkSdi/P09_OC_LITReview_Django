from django.contrib import admin
from .models import Review, BookToReview, TicketCreation, TicketToReview

# Register your models here.
admin.site.register(Review)
admin.site.register(BookToReview)
admin.site.register(TicketCreation)
admin.site.register(TicketToReview)
