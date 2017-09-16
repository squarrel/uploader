from django.conf.urls import url
from uploads import views


urlpatterns = [
    url(r'^documents', views.DocumentList.as_view(), name='documents'),
    url(r'^documents/(?P<pk>[0-9]+)/$', views.DocumentDetail.as_view(), name='document'),
]
