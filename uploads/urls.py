from django.conf.urls import url
from uploads import views


urlpatterns = [
    url(r'documents', views.DocumentView.as_view(), name='documents'),
]
