from django.shortcuts import render, redirect
from .models import Runner, Category, Competition, Time, Metas
from .forms import RunnerForm, MetasForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(resquest):
    runners = Runner.objects.all()
    categorys = Category.objects.all()
    return render(resquest, 'index.html', {'runners':runners})

def detail(request, slug):
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

def new_runner(request):
    if (request.method == 'POST'):
        form = RunnerForm(request.POST)
        if form.is_valid():
            runner = form.save(commit=False)
            runner.save()
            return HttpResponseRedirect('/members/new_runner/')
    else:
        form = RunnerForm()
        return render(request, 'new_runner.html', {'form':form} )


def metas(request, slug):
    run = Runner.objects.get(slug=slug)
    if (request.method == 'POST'):
        form = MetasForm(request.POST)
        if form.is_valid():

            metanew = Metas(meta = form.cleaned_data['meta'],
                         runner= run )
            metanew.save()
            return HttpResponseRedirect('/members/'+slug+'/metas/')
    else:
        metasuser = Metas.objects.filter(runner = run.id)
        form = MetasForm()
        return render(request, 'metas.html', {'form':form, 'metasuser':metasuser} )
