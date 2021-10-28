from django.urls import path
from .views import *

urlpatterns = [
    path('', AuthUserView.as_view())
]
