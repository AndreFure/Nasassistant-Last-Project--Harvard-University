from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment
from .forms import ListingForm, BidForm, CommentForm


def index(request):
    listings = Listing.objects.filter(is_active=True).order_by('-posted_date')
    return render(request, "nasassistant/index.html", {'listings': listings})


def day(request):
    return render(request, "nasassistant/day.html")


def mars(request):
    return render(request, "nasassistant/mars.html")


def form1(request):
    return render(request, "nasassistant/form1.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "nasassistant/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "nasassistant/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "nasassistant/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "nasassistant/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "nasassistant/register.html")


def exoplanets(request):
    return render(request, "nasassistant/exoplanets.html")


def exoplanets_comparison(request):
    return render(request, "nasassistant/exoplanets_comparison.html")
