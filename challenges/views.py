import django
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Go the whole month without eating anything with sugar!",
    "february": "Walk 20 minutes a day. This will get you close to the recommend 150 minutes a week of moderate exercise.",
    "march": "Choose a new talent and develop it for at least 20 minutes every day!",
    "april": "Clean your room!",
    "may": "Be grateful for something every day!",
    "june": "When you are outside observe the various plants an animals!",
    "july": "Meditate for 20 minutes everyday!",
    "august": "Create or optimize your budget!",
    "september": "Learn at least one new thing about an ancient empire everyday!",
    "october": "Try some food, especially treats, you haven't tried before!",
    "november": "Practice continued education. Keep up on changes in your profession or start on a new speciality/profession!",
    "december": "Increase the length and/or quality of sleep you get every night!"
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    if month > len(monthly_challenges):
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponseRedirect(reverse("month-challenge", args=[list(monthly_challenges.keys())[month - 1]]))


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"challenge_text": challenge_text,
                                                             "month_name": month})
    except:
        raise Http404()
