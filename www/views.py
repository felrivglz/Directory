from django.shortcuts import render
from .models import Person
# Create your views here.
def index(resquest):
    people = Person.objects.all()
    return render(resquest, 'index.html', {'people':people})
