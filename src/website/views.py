from itertools import chain
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, TicketForm
from login.models import CustomUser
from .models import Review, Ticket
from django.db.models import CharField, Value, Q


@login_required
def follow(request):
    context = {}
    user = CustomUser.objects.get(pk=request.user.id)
    if request.method == "POST":
        search = request.POST["search"]
        try:
            followed = CustomUser.objects.get(username=search)
            if followed is not None:  
                user.follows.add(followed)
                user.save()
        except:
            messages.error(request, f'{search} n\'existe pas')
            return redirect('follow-page')
        
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

@login_required
def ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            instance = ticket_form.save(commit=False)
            instance.user = request.user
            ticket_form.save()
            return redirect('feed')
        else:
            messages.error(request, "Erreur de POST")
    else:
        ticket_form = TicketForm()

    return render(request, "ticket.html", {"ticket_form": ticket_form})

@login_required
def review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if any([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('feed')
    else:
        review_form = ReviewForm()
    
    context = {"review_form": review_form, 
               "ticket_form":ticket_form}
           
    return render(request, "review.html", context)

@login_required
def feed(request):
    reviews = Review.objects.filter(
        Q(user__in=request.user.follows.all()) |
        Q(user=request.user) |
        Q(ticket__user=request.user) 
    ).distinct()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(
        Q(user__in=request.user.follows.all()) |
        Q(user=request.user)
    )
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews_and_tickets = sorted(chain(reviews, tickets), key=lambda x: x.time_created, reverse=True)
    
    context = {"reviews_and_tickets":reviews_and_tickets}
    
    return render(request, 'feed.html', context)

@login_required
def posts(request):
    reviews = Review.objects.filter(
        Q(user=request.user) |
        Q(ticket__user=request.user))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews_and_tickets = sorted(chain(reviews, tickets), key=lambda x: x.time_created, reverse=True)
    
    context = {"reviews_and_tickets":reviews_and_tickets}
    
    return render(request, 'posts.html', context)

@login_required
def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST or None, request.FILES or None, instance=ticket)
        if form.is_valid:
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('posts')
        else:
            form = TicketForm(instance=ticket)
        
    return render(request, "edit-ticket.html", {'form':form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.delete()
        
    return redirect('posts')

@login_required
def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    ticket = Ticket.objects.get(id=review.ticket.id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST or None, request.FILES or None, instance=review)
        if form.is_valid:
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('posts')
        else:
            form = ReviewForm(instance=ticket)
    
    context = {'form':form, 'ticket':ticket}
        
    return render(request, "edit-review.html", context)

@login_required
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
        
    return redirect('posts')

@login_required
def ticket_review(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST or None)
        if review_form.is_valid:
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('feed')
    else:
        review_form = ReviewForm()
    
    context = {"review_form": review_form, 
               "ticket": ticket}
    
    return render(request, "ticket-review.html", context)

