from django.contrib import admin

from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['customerid', 'productid', 'content', 'created']
    search_fields = ['customerid', 'productid', 'content', 'created']

admin.site.register(Comment, CommentAdmin)