from django.conf.urls import url

from EFiles.models import EFile
from . import views

app_name = 'EFiles'

urlpatterns = [
    # /efiles/
    url(r'^$', views.index, name='index'),

    # /efiles/register/
    url(r'^register/$', views.register, name='register'),

    # /efiles/logout_user/
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /efiles/login_user/
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /efiles/<efile_id>/
    url(r'^(?P<efile_id>[0-9]+)/$', views.detail, name='detail'),

    # /efiles/add
    url(r'^add/$', views.add_efile, name='add_efile'),

    # /efiles/update/<efile_id>/
    url(r'^update/(?P<efile_id>[0-9]+)/$', views.update_efile, name='efile-update'),

    # /efiles/delete/<efile_pk>/
    url(r'^delete/(?P<pk>[0-9]+)/$', views.EFileDelete.as_view(), name='efile-delete'),

    # /efiles/search/<query>
    url(r'^search/$', views.search, name='search'),

]
