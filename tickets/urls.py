from django.conf.urls import patterns, url
from django.contrib import admin

from impl_tickets import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tickets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^get_items/$', views.get_items, name='get_items'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^fix_item/$', views.fix_item, name='fix_item'),
    url(r'^delete_item/$', views.delete_item, name='delete_item'),
)
