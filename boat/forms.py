from django import forms
from django.forms import ModelForm
from .models import boat_details,user_details,ride_booking
#create a form for Boats
class boat_detailsForm(ModelForm):
    class Meta:
        model = boat_details
        fields = "__all__"
        
        widgets = {
            'boat_name':forms.Select(attrs={'class':'form-select','placeholder':'Boat Name'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'capacity':forms.NumberInput(attrs={'class':'form-control','placeholder':'capacity'}),
            'fee':forms.NumberInput(attrs={'class':'form-control','placeholder':'Fee'}),
            'postdate':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'})
        }
        
class user_loginForm(ModelForm):
    class Meta:
        model = user_details
        fields = ('name','gender','contact','email','password')
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'gender':forms.Select(attrs={'class':'form-select','placeholder':'Gender'}),
            'contact':forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }

class book_rideForm(ModelForm):
    class Meta:
        model = ride_booking
        fields = ('user','boat_name','no_of_pass','doj','contact','email')
        
        widgets = {
            'user':forms.Select(attrs={'class':'form-select','placeholder':'User'}),
            'boat_name':forms.Select(attrs={'class':'form-select','placeholder':'Baot Name'}),
            'no_of_pass':forms.NumberInput(attrs={'class':'form-control','placeholder':'Members'}),
            'doj':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'contact':forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }
        
class edit_passengersForm(ModelForm):
    class Meta:
        model = ride_booking
        fields = ('status',)
        
        widgets = {
            'status':forms.Select(attrs={'class':'form-select','placeholder':'status'}),
        }
        
