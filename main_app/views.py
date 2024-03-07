from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ring


class Home(LoginView):
  template_name='home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def ring_index(request):
  rings = Ring.objects.filter(user=request.user)
  return render(request, 'rings/index.html',
  { 'rings': rings })

@login_required
def ring_detail(request, ring_id):
  ring = Ring.objects.get(id=ring_id)
  return render(request, 'rings/detail.html', { 'ring': ring })

class RingCreate(LoginRequiredMixin, CreateView):
  model = Ring
  fields = ['name', 'status', 'size', 'metal', 'stone', 'condition', 'weight', 'price', 'purchase_point', 'purchase_date']
  success_url= '/inventory/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class RingUpdate(LoginRequiredMixin, UpdateView):
  model = Ring
  fields = ['name', 'status', 'size', 'metal', 'stone', 'condition', 'weight', 'price', 'purchase_point', 'purchase_date']

class RingDelete(LoginRequiredMixin, DeleteView):
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

@login_required
def purchase_index(request):
  return render(request, 'purchases/index.html')
