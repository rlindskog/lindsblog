from django.contrib import admin
from .models import Post

# Register your models here.

# if you have a form
# class PostAdmin(admin.ModelAdmin):
#     formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

# adds things next to your model
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'category', 'created', 'edited',]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)
