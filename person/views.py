from django.shortcuts import render, get_object_or_404
from .models import Person

# Create your views here.
def active_state_person_list(request):
    active_persons = Person.active.all()
    return render(request, 'person/active_state_person_list.html', {'active_persons': active_persons})

def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'person/person_detail.html', {'person': person})