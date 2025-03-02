from django.urls import path
from .views import GetAllUsersView

urlpatterns = [
    path('get-all-users/', GetAllUsersView.as_view(), name='get-all-users'),
]
