from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.home,name='home'),
    path('about', views.about,name='about'),
    # path('login_UI', views.login_UI,name='login_UI'),
    path('contact', views.contact,name='contact'),
    path('services', views.services,name='services'),
    # path('admin_login', views.admin_login,name='admin_login'),
    path('staff', views.staff,name='staff'),
    path('boatowners', views.boatowners,name='boatowners'),
    path('manageClients', views.manageClients,name='manageClients'),
    path('test', views.test,name='test'),
    path('add_boat', views.add_boat,name='add_boat'),
    path('view_edit_boat_details/<boat_details_id>', views.view_edit_boat_details,name='view_edit_boat_details'),
    path('delete_boat_details/<boat_details_id>', views.delete_boat_details,name='delete_boat_details'),
    path('accounts', views.accounts,name='accounts'),
    path('user_login', views.user_login,name='user_login'),
    path('register', views.register,name='register'),
    path('admin_view', views.admin_view,name='admin_view'),
    path('user_profile/<name>', views.user_profile,name='user_profile'),
    path('book_ride', views.book_ride,name='book_ride'),
    path('ride_log', views.ride_log,name='ride_log'),
    path('passengers', views.passengers,name='passengers'),
    path('delete_user_details/<user_details_id>', views.delete_user_details,name='delete_user_details'),
    path('bill/<ride_booking_id>', views.bill,name='bill'),
    path('transactions', views.transactions,name='transactions'),
    path('edit_passengers/<ride_booking_id>', views.edit_passengers,name='edit_passengers')

]