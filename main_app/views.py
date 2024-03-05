from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class RingCreate(CreateView):
  model = Ring
  fields = '__all__'
  success_url= '/inventory/'

class RingUpdate(UpdateView):
  model = Ring
  fields = '__all__'

class RingDelete(DeleteView):
  model = Ring
  fields = '__all__'
  success_url='/inventory/'

