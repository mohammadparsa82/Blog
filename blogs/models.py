from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name


class Post (models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE, null=True)
    title =  models.CharField(max_length=100)
    content = models.TextField()
    counted_views = models.IntegerField()
    published_date = models.DateTimeField()
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to= 'blog/', default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    class Meta:
        ordering = ['-created_date']
    #show title and id 
    def __str__(self):
        return "{} - {} ".format(self.id, self.title)
    
    def get_absolute_url(self):
        return reverse('blogs:single', kwargs={'pid':self.id})