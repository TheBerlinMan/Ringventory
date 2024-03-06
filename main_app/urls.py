from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('inventory/', views.ring_index, name='ring-index'),
  path('inventory/<int:ring_id>', views.ring_detail, name='ring-detail'),
  path('inventory/create/', views.RingCreate.as_view(), name='ring-create'),
  path('inventory/<int:pk>/update>', views.RingUpdate.as_view(), name='ring-update'),
  path('inventory/<int:pk>/delete>', views.RingDelete.as_view(), name='ring-delete'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
]