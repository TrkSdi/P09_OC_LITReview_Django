from django import forms
from .models import Review, Ticket, BookToReview, TicketToReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {"title": "Titre", 
                  "comment": "Commentaire",
                  "note": "Note"}
        widgets = {"note": forms.RadioSelect(),
                   "comment": forms.Textarea()}
        
class BookToReview(forms.ModelForm):
    class Meta:
        model = BookToReview
        fields = "__all__"
        labels = {"book_title": "Titre",
                  "description": "Description",
                  "image": "Image", 
                  "review_title": "Titre critique",
                  "comment": "Commentaire",
                  "note": "Note"}
        widgets = {"note": forms.RadioSelect(),
                   "comment": forms.Textarea(),
                   "description": forms.Textarea()}

class TicketToReview(forms.ModelForm):
    class Meta:
        model = TicketToReview
        fields = "__all__"
        labels = {"title": "Titre", 
                  "comment": "Commentaire",
                  "note": "Note"}
        widgets = {"note": forms.RadioSelect(),
                   "comment": forms.Textarea()}

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre", 
                  "description": "Description"}
        widgets = {"description": forms.Textarea()}
        
        
