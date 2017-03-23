from django.shortcuts import render, redirect
from .models import Runner, Category, Competition, Time, Metas
from .forms import RunnerForm, MetasForm, LoginForm, CompeForm, CompetenciaForm, CategoriaForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(resquest):
    runners = Runner.objects.all()
    categorys = Category.objects.all()
    return render(resquest, 'index.html', {'runners':runners})

def detail(request, username, slug):
    alltime=[]
    runner =Runner.objects.get(slug=slug)
    distance = runner.get_distance_display()
    times = Time.objects.filter(runner = runner.id)
    metasuser = Metas.objects.filter(runner = runner.id)
    for timede in times:

        alltime.append(
                        [
                            timede.distance,
                            timede.time,
                            timede.compentition.name,
                            timede.compentition.date
                        ])

    return render(request, 'details.html',{'runner':runner, 'distance':distance,
                                           'alltime': alltime,'metasuser':metasuser} )


def edit(request, slug):
    runner = Runner.objects.get(slug=slug)
    if (request.method == 'POST'):
        form = RunnerForm(request.POST,  instance=runner)
        if form.is_valid():
            runner=form.save(commit=False)
            runner.slug =slug
            runner.save()
        return redirect(reverse('detail', args=[slug,]))
    else:
        runner_dict = model_to_dict(runner)
        form = RunnerForm(runner_dict)

    return render(request, 'edit.html',{'form': form})

def new_runner(request, username):
    coach = User.objects.get(username = username)
    runners = Runner.objects.filter(coach=coach)
    if (request.method == 'POST'):
        form = RunnerForm(request.POST)
        if form.is_valid():
            runner = form.save(commit=False)
            runner.coach = coach
            runner.save()
            return HttpResponseRedirect('/coach/'+username+'/new_runner/')
    else:
        form = RunnerForm()
        return render(request, 'new_runner.html', {'form':form, 'runners':runners})

def categoria(request, username):
    cates =Category.objects.all()
    if (request.method == 'POST'):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return HttpResponseRedirect('/coach/'+username+'/categoria/')
    else:
        form = CategoriaForm()
        return render(request, 'categoria.html', {'form':form, 'cates':cates})


def competencia(request, username):
    compes =Competition.objects.order_by('-date')
    if (request.method == 'POST'):
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            compe = form.save(commit=False)
            compe.save()
            return HttpResponseRedirect('/coach/'+username+'/competencia/')
    else:
        form = CompetenciaForm()
        return render(request, 'competencias.html', {'form':form, 'compes':compes})


def metas(request, username, slug):
    run = Runner.objects.get(slug=slug)
    if (request.method == 'POST'):
        form = MetasForm(request.POST)
        if form.is_valid():

            metanew = Metas(meta = form.cleaned_data['meta'],
                         runner= run )
            metanew.save()
            return HttpResponseRedirect('/coach/'+username+'/metas/'+slug)
    else:
        metasuser = Metas.objects.filter(runner = run.id)
        form = MetasForm()
        return render(request, 'metas.html', {'form':form, 'metasuser':metasuser, 'slug':slug} )


def marcas(request, username, slug):
    run = Runner.objects.get(slug=slug)
    if (request.method == 'POST'):
        form = CompeForm(request.POST)
        if form.is_valid():
            newtime = Time(distance = form.cleaned_data['distance'], compentition = form.cleaned_data['compentition'],
                           runner = run, time = form.cleaned_data['time'])
            newtime.save()
            return HttpResponseRedirect('/coach/'+username+'/marcas/'+slug)
    else:
        tuser = Time.objects.filter(runner = run.id)
        form = CompeForm()
        return render(request, 'tiempos.html', {'form':form, 'tuser':tuser, 'slug':slug} )



def login_view(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/coach/'+user.username+'/athletes')
                else:
                    form=LoginForm()
                    return render(request, 'login.html', {'form':form, 'nel':"nel1"})
            else:
                form=LoginForm()
                return render(request, 'login.html', {'form':form, 'nel':"nel2"})
    else:
        form=LoginForm()
        return render(request, 'login.html', {'form':form, 'nel':"nel"})

def logout_view(request):
    logout(request)
    return index(request)


def athletes(request, username):
        if username != '':
            coach = User.objects.get(username=username)
            runners = Runner.objects.filter(coach=coach)
            return render(request, 'athletes.html', {'runners':runners})
        else:
            form=LoginForm()
            return render(request, 'login.html', {'form':form})
