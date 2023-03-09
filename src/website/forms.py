from django import forms
from .models import Review, Ticket



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", 
                  "rating", 
                  "body"]
        labels = {"headline": "Titre", 
                  "body": "Commentaire",
                  "rating": "Note"}
        widgets = {"rating": forms.RadioSelect(),
                   "comment": forms.Textarea()}
        
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre", 
                  "description": "Description",
                  "image": "Image"}
        widgets = {"description": forms.Textarea()}      
        
        
