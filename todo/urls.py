from django.conf.urls import patterns, url
from todo import views

urlpatterns = patterns('',
    url(r"^mark_done/(\d*)/$", views.mark_done),
    url(r"^mark_done2/(\d*)/$", views.mark_done2),
    url(r"^item_action/(done|delete|onhold)/(\d*)/$", views.item_action),
)