from django.shortcuts import render

class Ring:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

inventory = [
  Ring('Lolo', 'tabby', 'Kinda rude.', 3),
  Ring('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Ring('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Ring('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def ring_index(request):
  return render(request, 'ring/index.html',
  { 'inventory': inventory })