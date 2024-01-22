from django.db import models

# Create your models here.
class Post (models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    counted_views = models.IntegerField()
    published_date = models.DateTimeField()
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

    #show title and id 
    def __str__(self):
        return "{} - {} ".format(self.id, self.title)