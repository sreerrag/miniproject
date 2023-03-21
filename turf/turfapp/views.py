from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from .models import Turf,Booking
from django.contrib.auth.forms import UserCreationForm


class Turflist(ListView):
    model = Turf
    context_object_name = 'turf'
    template_name = 'turflist.html'


class Bookturf(CreateView):
    model = Booking
    fields = '__all__'
    success_url = reverse_lazy('turf')
    template_name = 'booking.html'


class Viewbooking(ListView):
    model = Booking
    context_object_name = 'viewbooking'
    template_name = 'viewbooking.html'

class Editbooking(UpdateView):
    model = Booking
    fields = '__all__'
    success_url = reverse_lazy('viewbooking')
    template_name = 'booking.html'

class DeleteBooking(DeleteView):
    model = Booking
    context_object_name = 'booking'
    success_url = reverse_lazy('viewbooking')
    template_name = 'bookingdelete.html'


class BookingDetailView(DetailView):
    model = Booking
    template_name = 'detailbooking.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'



class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('turf-list')

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')

def Home(request):
    return render(request,"home.html")