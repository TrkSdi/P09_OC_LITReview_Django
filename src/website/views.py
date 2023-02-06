from django.shortcuts import render
from django.contrib import messages
from .forms import ReviewForm, TicketForm, BookToReview, TicketToReview


def feed(request):
    return render(request, "flux.html")

def posts(request):
    return render(request, "posts.html")

def followers(request):
    return render(request, "follow.html")

def review(request):
    if request.method == 'POST':
        review_form = BookToReview(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save()
            review_form.clean()
    else:
        review_form = BookToReview()
           
    return render(request, "review.html", {"review_form": review_form})

def edit_review(request):
    return render(request, "edit-review.html")

def ticket(request):
    
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket_form.save()
        else:
            messages.error(request, "Erreur de POST")
    else:
        ticket_form = TicketForm()

    return render(request, "ticket.html", {"ticket_form": ticket_form})


def ticket_review(request):
    if request.method == 'POST':
        review_form  = TicketToReview(request.POST)
        if review_form.is_valid():
            review_form.save()
            review_form.clean()
    else:
        review_form = TicketToReview()
            
    return render(request, "ticket-review.html", {"review_form": review_form})

def edit_ticket(request):
    return render(request, "edit-ticket.html")