from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('post/<int:pk>', views.post, name='post')
]
