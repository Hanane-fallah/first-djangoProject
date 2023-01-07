from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'views'
urlpatterns = [
    path('', TemplateView.as_view(template_name='views/main.html')),
    path('funky', views.funky, name='funky'),
    path('danger', views.danger, name='danger'),
    path('rest/<int:guess>', views.rest, name='rest'),
    path('remain/<int:guess>', views.RestMainView.as_view(), name='remainview'),
    path('bounce/', views.bounce)
]
