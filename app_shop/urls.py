from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

f = open('log.cookie', 'w')
f.truncate()
f.write(str(0))
f.close()

urlpatterns = [
    url(r'^$', views.books_list, name='books_list'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^category/(?P<pk>[a-z]+)/$', views.category, name='category'),
    url(r'^buy/(?P<pk>[0-9]+)/$', views.buy, name='buy'),
    url(r'^writereview/(?P<pk>[0-9]+)/$', views.writereview, name='writereview'),
    url(r'^acountdetails//$', views.acountdetails, name='acountdetails')
]
