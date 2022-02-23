from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', { 'plant': plant})

def seasons(request):
    return render(request, 'plants/seasons/all.html')

def spring(request):
    bloom = Plant.objects.all().filter(bloom_season='SPG')
    trim = Plant.objects.all().filter(trim_season='SPG')
    return render(request, 'plants/seasons/spring.html', { 'bloom': bloom, 'trim': trim })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = [ 'name',
        'scientific_name',
        'description',
        'type',
        'height',
        'spread',
        'bloom_season',
        'trim_season' ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['scientific_name',
        'description',
        'type',
        'height',
        'spread',
        'bloom_season',
        'trim_season' ]
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('index')
        return super(PlantUpdate, self).dispatch(request, *args, **kwargs)

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('index')
        return super(PlantDelete, self).dispatch(request, *args, **kwargs)