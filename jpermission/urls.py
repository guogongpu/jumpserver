from django.conf.urls import patterns, include, url


urlpatterns = patterns('jpermission.views',
    # Examples:
    # url(r'^$', 'jumpserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^perm_host/$', 'perm_host'),
    (r'^perm_add/$', 'perm_add'),
    (r'^perm_user_show/$', 'perm_user_show'),
    (r'^perm_list/$', 'perm_list'),
)
