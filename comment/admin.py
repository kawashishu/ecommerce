from django.contrib import admin

from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'content', 'created']
    search_fields = ['customer', 'product', 'content', 'created']


admin.site.register(Comment, CommentAdmin)
