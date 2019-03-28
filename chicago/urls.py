"""chicago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views

from . views import welcome, SignUpView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Auth
    url(r'login$', views.LoginView.as_view(), name="login"),
    url(r'logout$', views.LogoutView.as_view(), name="logout"),
    url(r'signup$', SignUpView.as_view(), name='signup'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^volunteer/', include('volunteer_admin.urls')),
    url(r'^page/', include('frontend.urls')),
    url(r'^$', welcome, name="welcome")
]
