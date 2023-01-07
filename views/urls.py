from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'views'
urlpatterns = [
    path('', TemplateView.as_view(template_name='views/main.html')),
    path('funky', views.funky),
    path('danger', views.danger)
]