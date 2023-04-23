from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

alpha = RegexValidator(r'^[a-z A-Z]*$', 'Only Alphabet characters are allowed.')

boat_names = [('Coble','Coble'),('Jet Ski','Jet Ski'),('Small Yacht','Small Yacht'),('Inflatable Boat','Inflatable Boat'),('Speedboat','Speedboat'), ('Big Yacht','Big Yacht')]
gender = [('Male','Male'),('Female','Female'),('Other','Other')]
status=[('Paid','Paid'),('Pending','Pending')]

class boat_details(models.Model):
    boat_name = models.CharField( max_length=50,choices=boat_names,null=False)
    capacity = models.PositiveIntegerField(null=False)
    fee = models.PositiveIntegerField(null=False)
    postdate = models.DateField()

    def __str__(self):
        return self.boat_name 

class user_details(models.Model):
    name = models.CharField(max_length=25,validators=[alpha])
    gender=models.CharField(max_length=10,choices=gender)
    contact=models.PositiveBigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=25)    

    def __str__(self):
        return self.name 

class ride_booking(models.Model):
    user = models.ForeignKey(user_details,on_delete=models.CASCADE, null=True )
    boat_name = models.ForeignKey(boat_details,on_delete=models.CASCADE, null=True)
    no_of_pass = models.PositiveIntegerField()
    doj = models.DateField()
    email = models.EmailField()
    contact = models.PositiveBigIntegerField()
    status = models.CharField(max_length=25,choices=status,default='Pending')

    def amt(self):
        
        return self.boat_name.fee
    def __str__(self):
        return self.user.name

class invoice(models.Model):
    usern = models.ForeignKey(user_details,on_delete=models.DO_NOTHING, null=True )
    boat = models.ForeignKey(boat_details,on_delete=models.DO_NOTHING, null=True)
    AMT = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.usern
    
    def __str__(self):
        return self.boat
    def __str__(self):
        return self.AMT