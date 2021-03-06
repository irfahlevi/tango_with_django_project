from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^page/(?P<slug>[\w\-]+)/$', views.show_page, name='show_page'),

    # chap6
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),

    # chap7
    url(r'^add_category/$', views.add_category, name='add_category'),

    # url(r'^add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),


    # chap9
    url(r'^register/$', views.register, name='register'),  # New pattern!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),


]


