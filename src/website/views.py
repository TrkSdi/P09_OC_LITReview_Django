from django.shortcuts import render
from django.contrib import messages
from .forms import ReviewForm, TicketForm


def feed(request):
    return render(request, "flux.html")

def posts(request):
    return render(request, "posts.html")

def followers(request):
    return render(request, "follow.html")

def review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            review_form.clean()
    else:
        review_form = ReviewForm()
           
    return render(request, "review.html", {"review_form": review_form})

def edit_review(request):
    return render(request, "edit-review.html")

def ticket(request):
    
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        print("Step1 :")
        if ticket_form.is_valid():
            print("Step2: ", ticket_form)
            ticket = ticket_form.save()
            print("ticket_ID:", ticket.id)
        else:
            print("Error else")
            print(ticket_form.errors)
            messages.error(request, "Erreur de POST")
              
    else:
        ticket_form = TicketForm()

    return render(request, "ticket.html", {"ticket_form": ticket_form})

def ticket_review(request):
    return render(request, "ticket-review.html")

def edit_ticket(request):
    return render(request, "edit-ticket.html")