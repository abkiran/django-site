from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views
from django.urls import reverse_lazy

from . views import SignUpView, anonymous_required

urlpatterns = [
    # Auth
    url('login/', anonymous_required(views.LoginView.as_view()), name="login"),
    url('logout/', views.LogoutView.as_view(), name="logout"),
    url('signup/', SignUpView.as_view(), name='signup'),
    path('password-reset/', anonymous_required(views.PasswordResetView.as_view(success_url = reverse_lazy('login'))), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]