from django.urls import path, re_path
from . import views
from django.conf.urls.static import static

urlpatterns= [
    #
    # re_path(r'^$',views.index, name='index')
    path('',views.index, name='index'),
    re_path(r'^details/(?P<id>\d+)/$',views.details, name='details')
];
