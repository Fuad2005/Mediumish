from django.shortcuts import render, get_object_or_404
from info.models import Stories

# Create your views here.
def post(request,pk):
    stories = get_object_or_404(Stories, pk = pk)
    tags = stories.tags.all()
    related = Stories.objects.order_by('?').exclude(pk=stories.pk)[:3]


    return render(request, 'post.html', context={
        'stories': stories,
        'tags': tags,
        'related': related
    })

