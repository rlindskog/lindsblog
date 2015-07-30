from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.blog', name='blog'),
]