from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhoneList.as_view()),
    path('phone_detail', views.PhoneDetail.as_view()),
]