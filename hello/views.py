from django.shortcuts import render
from datetime import date


def is_it_christmas(request):
    today = date.today()
    is_christmas = "Yes" if today.month == 12 and today.day == 25 else "No"
    return render(request, 'index.html', {'is_christmas': is_christmas})
