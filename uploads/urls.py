from django.conf.urls import url
from uploads import views


urlpatterns = [
    url(r'uploads', views.DocumentView.as_view()),
]
