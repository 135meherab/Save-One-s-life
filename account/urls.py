from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', views.activate_account, name='activate'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout')
]
