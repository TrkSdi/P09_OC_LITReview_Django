from django import forms
from .models import Review, TicketCreation


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {"title": "Titre", 
                  "comment": "Commentaire",
                  "note": "Note"}
        widgets = {"note": forms.RadioSelect(),
                   "comment": forms.Textarea()}
        

class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketCreation
        fields = ["title", "description", "image"]
        labels = {"title": "Titre", 
                  "description": "Description"}
        widgets = {"description": forms.Textarea(),
                   "image": forms.FileInput()}
        
