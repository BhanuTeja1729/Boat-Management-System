from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib import messages
from django.db.models import Sum
from .models import boat_details, user_details, ride_booking,invoice
from .forms import boat_detailsForm,user_loginForm,book_rideForm,edit_passengersForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# def login_UI(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return redirect('staff')
#         else:
#             messages.success(request, "there was an error Logging in, Try Again ... ")
#             # Return an 'invalid login' error message.
#             return redirect('login_UI')
#     else:
#         return render(request, 'login_UI.html')

# def admin_login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return redirect('staff/')
#         else:
#             messages.success(request, "there was an error Logging in, Try Again ... ")
#             # Return an 'invalid login' error message.
#             return redirect('admin_login')
#     else:
#         return render(request, 'admin_login.html')

def staff(request):
    boats = boat_details.objects.all()
    passengers = ride_booking.objects.all()
    boats_total = boats.count()
    passengers_total = passengers.count()
    return render(request, 'staff.html',{'boats_total': boats_total,'passengers_total': passengers_total})

def services(request):
    return render(request, 'services.html')

def boatowners(request):
    return render(request, 'boatowners.html')

def manageClients(request):
    allclients = user_details.objects.all()
    return render(request, 'manageClients.html',{'allclients':allclients})

def test(request):
    all_boats = boat_details.objects.all()
    return render(request, 'test.html',{'all_boats':all_boats})

def accounts(request):
    return render(request, 'accounts.html')

def passengers(request):
    history=ride_booking.objects.all()
    return render(request, 'passengers.html',{'history':history})

def ride_log(request):
    history=ride_booking.objects.all()
    return render(request, 'ride_log.html',{'history':history})

@login_required(login_url='user_login')
def user_profile(request,name):
    user=user_details.objects.get(name=name )
    return render(request, 'user_profile.html',{'user':user})

def user_login(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        try:
            user=user_details.objects.get(name=name,password=password)
            return redirect('user_profile',name)
                
        except:
            messages.info(request, 'There was an error Logging in. Please check Yor Password ... ')
            return redirect('user_login')
       
    else:
        return render(request, 'user_login.html')

def logout(request):
    currentUser=request.user
    logout(currentUser)
    return redirect('user_login')


def register(request):
    if request.method == "POST":
        form = user_loginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            messages.info(request,'Please Check your Username. Username Should be in Alphabets...')
            return redirect('register')
        
    form = user_loginForm  
    return render(request, 'register.html',{'form':form})

def admin_view(request):
    if request.method=='POST':
        username=request.POST['username'] 
        password=request.POST['password']
        user = authenticate(request, username=username, password=password,is_superuser=True)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('staff')
        else:
            messages.info(request, "there was an error Logging in, Try Again ... ")
            return redirect('accounts')
        
    return render(request,'staff.html')


@login_required
def add_boat(request):
    if request.method == "POST":
        form = boat_detailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')
        
    form = boat_detailsForm  
    return render(request, 'add_boat.html',{'form':form,})

def view_edit_boat_details(request,boat_details_id):
    boat_details_info=boat_details.objects.get(id=boat_details_id)
    form = boat_detailsForm(request.POST or None,instance = boat_details_info)
    if form.is_valid():
        form.save()
        return redirect('test')
    
    return render(request, 'view_edit_boat_details.html',{'form':form})
def edit_passengers(request,ride_booking_id):
    ride_booking_info=ride_booking.objects.get(id=ride_booking_id)
    form = edit_passengersForm(request.POST or None,instance = ride_booking_info)
    if form.is_valid():
        form.save()
        return redirect('staff')
    return render(request, 'edit_passengers.html',{'form':form})

def delete_boat_details(request,boat_details_id):
    get_bd=boat_details.objects.get(id=boat_details_id)
    get_bd.delete()
    details=boat_details.objects.all()
    details_count=boat_details.objects.count()

    return render(request, 'test.html',{'details':details,'details_count':details_count})

@login_required(login_url='user_login')
def book_ride(request):
    
    if request.method == "POST":
        form = book_rideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ride_log')
        
    form = book_rideForm 
    history=boat_details.objects.all()
    return render(request, 'book_ride.html',{'form':form,'history':history})

def delete_user_details(request,user_details_id):
    get_ud=user_details.objects.get(id=user_details_id)
    get_ud.delete()
    details=user_details.objects.all()
    details_count=user_details.objects.count()

    return render(request, 'passengers.html',{'details':details,'details_count':details_count})


def bill(request,ride_booking_id):
    ride_details_info=ride_booking.objects.get(id=ride_booking_id)
    return render(request, 'bill.html',{'ride_details_info':ride_details_info})


def transactions(request):
    history=ride_booking.objects.all()
    boats_total = history.count()
    return render(request, 'transactions.html',{'boats_total': boats_total,'history':history})