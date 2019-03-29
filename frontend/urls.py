from django.conf.urls import url, include
from .views import welcome

urlpatterns = [
    url(r'^page/', welcome),
    url('', welcome, name='landing_page'),
]