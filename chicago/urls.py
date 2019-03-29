from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Auth
    path('accounts/', include('accounts.urls')),

    path('volunteer', include('volunteer.urls'), name="volunteer_admin"),
    path('volunteer/', include('volunteer.urls'), name="volunteer_admin"),

    # url('', include('frontend.urls'))
]
