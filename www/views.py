from django.shortcuts import render
from .models import Runner, Category
# Create your views here.
def index(resquest):
    runners = Runner.objects.all()
    categorys = Category.objects.all()
    return render(resquest, 'index.html', {'runners':runners, 'categorys':categorys})
