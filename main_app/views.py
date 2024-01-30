from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Dog

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogindex(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog': dog })

class DogList(ListView):
    model = Dog

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/{id}'

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogindex'