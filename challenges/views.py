from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Go the whole month without eating anything with sugar!",
    "february": "Walk 20 minutes a day. This will get you close to the reccommend 150 minutes a week of moderate exercise.",
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


def monthly_challenge_by_number(request, month):
    if month > len(monthly_challenges):
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponseRedirect(reverse("month-challenge", args=[list(monthly_challenges.keys())[month - 1]]))


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}<h1/>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
