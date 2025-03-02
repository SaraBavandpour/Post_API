from django.urls import path
from .views import UserProfileListCreate

urlpatterns = [
    path('userprofiles/', UserProfileListCreate.as_view(), name='userprofile-list-create'),
]
