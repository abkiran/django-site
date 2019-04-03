from django.conf.urls import url
from django.urls import path
from crud import views


urlpatterns = [
    path('language/', views.LanguageList.as_view(), name='language_list'),
    path('language/<int:pk>', views.LanguageDetail.as_view(), name='language_detail'),
    path('language/create', views.LanguageCreate.as_view(), name='language_create'),
    path('language/update/<int:pk>', views.LanguageUpdate.as_view(), name='language_update'),
    path('language/delete/<int:pk>', views.LanguageDelete.as_view(), name='language_delete'),

]