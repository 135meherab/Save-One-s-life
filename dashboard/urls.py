from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('fileter/<slug:blood_slug>', views.dashboard, name= 'filter'),
    path('blood_request/', views.BloodRequestView.as_view(), name='blood_request'),
    path('accept/<int:id>/', views.Accept, name='accept'),
    path('donation_history/', views.DonateHistory, name='donation_history'),
    path('donation_history/donation/done/<int:id>', views.donation_done, name='donation_done'),
    path('donation_history/donation/cancel/<int:id>', views.donation_cancel, name='donation_cancel'),
]
