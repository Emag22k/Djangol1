from django.urls import path
from. import views

urlpatterns = [
    path('',views.home_page),
    path('about',views.about_page),
    path('phone',views.phone_page)
]