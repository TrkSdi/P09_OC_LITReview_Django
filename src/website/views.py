from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, TicketForm, BookToReview, TicketToReview
from login.models import CustomUser

@login_required
def feed(request):
    return render(request, "flux.html")

@login_required
def posts(request):
    return render(request, "posts.html")

@login_required
def review(request):
    if request.method == 'POST':
        review_form = BookToReview(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save()
            review_form.clean()
    else:
        review_form = BookToReview()
           
    return render(request, "review.html", {"review_form": review_form})

@login_required
def edit_review(request):
    return render(request, "edit-review.html")

@login_required
def ticket(request):
    
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            instance = ticket_form.save(commit=False)
            instance.user = request.user
            ticket_form.save()
            ticket_form = TicketForm()
        else:
            messages.error(request, "Erreur de POST")
    else:
        ticket_form = TicketForm()

    return render(request, "ticket.html", {"ticket_form": ticket_form})

@login_required
def ticket_review(request):
    if request.method == 'POST':
        review_form  = TicketToReview(request.POST)
        if review_form.is_valid():
            review_form.save()
            review_form.clean()
    else:
        review_form = TicketToReview()
            
    return render(request, "ticket-review.html", {"review_form": review_form})

@login_required
def edit_ticket(request):
    return render(request, "edit-ticket.html")

@login_required
def follow(request):
    if request.method == "GET":
        if "search" in request.GET:
            search = request.GET["search"]
            follower = CustomUser.objects.filter(username=search)
        else:
            messages.error(request, 'Utilisateur inexistant')
            
    return render(request, "follow.html", {"follower": follower})