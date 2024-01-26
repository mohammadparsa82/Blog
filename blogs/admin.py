from django.contrib import admin
from blogs.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author','counted_views','published_date','status','created_date', 'image' )
    list_filter = ('status','published_date','author',)
    search_fields = ['title', 'content']
admin.site.register(Post,PostAdmin)