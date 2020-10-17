from django.contrib import admin
from . import models
# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_title', 'alink', 'user_name', 'comment', 'sentiments')
    # id, phone_title, alink, user_name, comment, sentiments
    search_fields = ('phone_title', 'user_name',)
    list_filter = ('phone_title',)
    ordering = ('id', )

admin.site.register(models.Comments, CommentsAdmin)