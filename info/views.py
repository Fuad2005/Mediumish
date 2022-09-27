from django.shortcuts import render
from .models import Stories
# Create your views here.
def home(request):
    blogs = Stories.objects.all()
    checked = Stories.objects.filter(featured=True)
    search_value = request.GET.get('search')
    if request.GET.get('search'):
        blogs = blogs.filter(title__icontains=search_value)
        checked = checked.filter(title__icontains=search_value)

    return render(request, 'index.html', context={
        'blogs': blogs,
        'checked': checked
    })