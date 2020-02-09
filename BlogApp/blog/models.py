from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)

    #Foreign Key many to one
    #many -> posts
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    body = models.TextField()


    #Good practice:overriding str and get_absolute_url
    def __str__(self):
        return self.title


    #For forms => where data is send
    #Reverse -> reference an object by it's URL template name
    #post detail in urls.py
    #so after click on submit in form -> redirect to the detail page of new post
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)]) #ex:return '' -> remain on the same page (with the form)
