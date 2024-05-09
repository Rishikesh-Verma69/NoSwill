from django.urls import path, include
from .views import inventoryItemsView, UserProfileView, donationView

urlpatterns = [
    path('inventoryItems/', inventoryItemsView.as_view() , name='inventoryItems' ),
    path('userProfile/', UserProfileView.as_view() , name='userProfile' ),
    path('donation/', donationView.as_view(), name='donation')
]
