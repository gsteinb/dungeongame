from django.shortcuts import render
from django.http import HttpResponse
from.creation_forms import CreationForm

def creation(request):
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.valid():
            print(form.cleaned_data)
    else:
        form = CreationForm()
    return render(request, 'character_creation/character_creation.html', {'form': form})
