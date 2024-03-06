from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Ring


class Home(LoginView):
  template_name='home.html'

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

  def form_valid(self, form):
    form.instnace.user = self.request.user
    return super().form_valid(form)
  

class RingUpdate(UpdateView):
  model = Ring
  fields = '__all__'

class RingDelete(DeleteView):
  model = Ring
  fields = '__all__'
  success_url='/inventory/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('ring-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
