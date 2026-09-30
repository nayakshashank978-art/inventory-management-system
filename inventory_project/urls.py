from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    # Frontend pages served by Django
    path('', TemplateView.as_view(template_name='index.html'), name='dashboard'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('categories/', TemplateView.as_view(template_name='categories.html'), name='categories'),
]
