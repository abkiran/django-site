from django.conf.urls import url
from .views import welcome, dashboard


urlpatterns = [
    url(r'^page/', welcome),
    url('', dashboard, name='volunteer_dashboard'),

]