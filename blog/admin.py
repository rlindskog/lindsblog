from django.contrib import admin
from .models import Post

# Register your models here.

# if you have a form
# class PostAdmin(admin.ModelAdmin):
#     formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

admin.site.register(Post)
