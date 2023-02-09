from itertools import chain
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, TicketForm, BookToReview, TicketToReview
from login.models import CustomUser
from django.db.models import CharField, Value

@login_required
def feed(request):
    
    return render(request, 'flux.html', context={'posts': posts})
    

@login_required
def posts(request):
    return render(request, "posts.html")

@login_required
def review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            instance = review_form.save(commit=False)
            instance.user = request.user
            review_form.save()
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()
           
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
    context = {}
    user = CustomUser.objects.get(pk=request.user.id)
    print(request.method)
    if request.method == "POST":
        search = request.POST["search"]
        followed = CustomUser.objects.get(username=search)
        if followed is not None:  
            user.follows.add(followed)
            user.save()
    else:
        messages.error(request, 'Utilisateur inexistant')
            
    context = {"follows":user.follows.all(), "followed_by": user.followed_by.all()}
    
    return render(request, "follow.html", context)

@login_required
def unfollow(request):
    context = {}
    user = CustomUser.objects.get(pk=request.user.id)
    print(request.method)
    if request.method == "POST":
        followed_id = request.POST["followed_id"]
        followed = CustomUser.objects.get(pk=followed_id)
        if followed is not None:  
            user.follows.remove(followed)
            user.save()
    else:
        messages.error(request, 'Utilisateur inexistant')
            
    context = {"follows":user.follows.all(), "followed_by": user.followed_by.all()}
    
    return render(request, "follow.html", context)