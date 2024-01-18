from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('update/', views.UserUpdateView.as_view(), name='user_update'),
]
