from django.conf.urls.default import *

urlpatterns = patterns('',
    url('r^profile/($<profile_id\d+/$', 'user_profile.views.profile'),
    url('r^update_profile/$', 'user_profile.views.update_profile'),
    url('r^your_profile/$', 'user_profile.views.your_profil'),

)