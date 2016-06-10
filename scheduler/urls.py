from django.conf.urls import include, url
from django.conf import settings

import scheduler.views
import scheduler.api_views
import allauth.account.views


urlpatterns = [
    url(r'^$', allauth.account.views.login),

    url(r'^posts/list/$', scheduler.views.scheduled_posts_list, name="scheduled_posts_list"),
    url(r'^posts/add/$', scheduler.views.scheduled_posts_add, name="scheduled_posts_add"),
    url(r'^posts/edit/(?P<id>\d+)/$', scheduler.views.scheduled_posts_edit, name="scheduled_posts_edit"),
    url(r'^posts/delete/(?P<id>\d+)/$', scheduler.views.scheduled_posts_delete, name="scheduled_posts_delete"),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

# API Patterns
urlpatterns += [
    url(r'^api/post/add/$', scheduler.api_views.post_add),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/', include('django.contrib.staticfiles.urls')),
    ]
