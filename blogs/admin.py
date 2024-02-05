from django.contrib import admin
from blogs.models import Post ,Category , comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author','counted_views','published_date','status','created_date', 'image' )
    list_filter = ('status','published_date','author',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved',)
    search_fields = ['name', 'post']

admin.site.register(comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
