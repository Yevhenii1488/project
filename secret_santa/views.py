from django.shortcuts import render, redirect
from .models import Participant
from .forms import ParticipantForm
import random


def participant_list(request):
    participants = Participant.objects.all()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()

    return render(request, 'participant_list.html', {'participants': participants, 'form': form})


def secret_santa_randomizer(request):
    participants = list(Participant.objects.all())

    if len(participants) < 2:
        return render(request, 'randomizer.html',
                      {'error': 'At least two participants are required to run the Secret Santa game.'})

    random.shuffle(participants)
    pairs = list(zip(participants, participants[1:] + participants[:1]))

    attempts = 0
    while any(giver == receiver for giver, receiver in pairs) and attempts < 100:
        random.shuffle(participants)
        pairs = list(zip(participants, participants[1:] + participants[:1]))
        attempts += 1

    if any(giver == receiver for giver, receiver in pairs):
        return render(request, 'randomizer.html',
                      {'error': 'Unable to generate valid pairs. Please try again.'})

    return render(request, 'randomizer.html', {'pairs': pairs})


def clear_participants(request):
    Participant.objects.all().delete()
    return redirect('participant_list')
