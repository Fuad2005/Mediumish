from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author', kwargs={"pk": self.pk})


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    

    def __str__(self):
        return self.tag


class Stories(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(Author, null=True, on_delete= models.CASCADE,related_name="authors")
    date = models. DateField(auto_now_add= True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField()
    featured = models.BooleanField(default=False)   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"pk": self.pk})
        