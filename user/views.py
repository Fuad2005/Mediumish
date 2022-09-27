from django.shortcuts import render, get_object_or_404
from info.models import Author, Stories

# Create your views here.
def profile(request, pk):
    author = get_object_or_404(Author, pk = pk)
    blogs = Stories.objects.filter(author = author)
    

    return render(request, 'author.html', context={
        'author': author,
        'blogs': blogs
    })