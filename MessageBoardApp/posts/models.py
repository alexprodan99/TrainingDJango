from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()




    #post name => by default Post Object
    def __str__(self):
        return self.text[:50]
    