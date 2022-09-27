from django.contrib import admin
from .models import Stories, Tag,Author

# Register your models here.
admin.site.register(Stories)
admin.site.register(Author)
admin.site.register(Tag)