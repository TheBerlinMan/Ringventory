from django.shortcuts import render
from .models import Ring


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def ring_index(request):
  rings = Ring.objects.all()
  return render(request, 'rings/index.html',
  { 'rings': rings })

def ring_detail(request, ring_id):
  ring = Ring.objects.get(id=ring_id)
  return render(request, 'rings/detail.html', { 'ring': ring })