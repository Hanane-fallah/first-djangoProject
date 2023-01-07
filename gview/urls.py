from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'gview'
urlpatterns = [
    path('', TemplateView.as_view(template_name='gview/main.html')),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat/<int:pk>', views.CatDetailView.as_view(), name='cat'),

]