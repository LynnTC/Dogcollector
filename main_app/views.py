from django.shortcuts import render

dogs = [
  {'name': 'Zoey', 'breed': 'St. Bernard', 'description': 'playful and friendly', 'age': 10},
  {'name': 'Donut', 'breed': 'Corgi', 'description': 'loyal and protective', 'age': 10},
  {'name': 'Hino', 'breed': 'Appenzeller', 'description': 'blind', 'age': 6},
  {'name': 'Cheyenne', 'breed': 'Technically a cat', 'description': 'confused', 'age': 4},
  {'name': 'Frank', 'breed': 'Corgi/Husky', 'description': 'intelligent and graceful', 'age': 8},
  {'name': 'Willow', 'breed': 'dachshund', 'description': 'sweet and affectionate', 'age': 4},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogindex(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })