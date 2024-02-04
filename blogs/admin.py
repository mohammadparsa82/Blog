from django.contrib import admin
from blogs.models import Post ,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author','counted_views','published_date','status','created_date', 'image' )
    list_filter = ('status','published_date','author',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
