from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.active, name='active'),
]