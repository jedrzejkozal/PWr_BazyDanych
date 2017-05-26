from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.books_list, name='books_list'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
]
