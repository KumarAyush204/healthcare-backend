
from django.urls import path
from .views import UserManagement
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns=[
    path("register/",UserManagement.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]