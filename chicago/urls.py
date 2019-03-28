from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views
from django.urls import reverse_lazy

from . views import welcome, SignUpView, anonymous_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Auth
    url(r'login$', anonymous_required(views.LoginView.as_view()), name="login"),
    url(r'logout$', views.LogoutView.as_view(), name="logout"),
    url(r'signup$', SignUpView.as_view(), name='signup'),
    path('password-reset/', anonymous_required(views.PasswordResetView.as_view(success_url = reverse_lazy('login'))), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^volunteer/', include('volunteer_admin.urls')),
    url(r'^page/', include('frontend.urls')),
    url(r'^$', welcome, name="welcome")
]
