from django.urls import path
from.views import Turflist,Bookturf,Viewbooking,Editbooking,DeleteBooking,BookingDetailView,SignUpView,LoginView,LogoutView
from . import views

urlpatterns = [
    path('turf-list',Turflist.as_view(),name = 'turf'),
    path('book-turf/<int:pk>',Bookturf.as_view(),name = 'book-turf'),
    path('view-booking',Viewbooking.as_view(),name = 'viewbooking'),
    path('booking-update/<int:pk>',Editbooking.as_view(),name = 'booking-update'),
    path('booking-delete/<int:pk>', DeleteBooking.as_view(), name='booking-delete'),
    path('booking-detail/<int:pk>', BookingDetailView.as_view(), name = 'booking-detail'),
    path("register/",SignUpView.as_view(), name = 'register'),
    path("login/",LoginView.as_view(), name = 'login'),
    path("logout",LogoutView.as_view(),name = 'logout'),
    path("home/",views.Home)

]