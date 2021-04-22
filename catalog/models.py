from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
# Create your models here.
from datetime import date


##################   general model #############################
class ActivityUser(models.Model):
    identity =  models.CharField(max_length=10)
    name = models.CharField(max_length=12)
    department = models.CharField(max_length=10)
    e_mail =  models.EmailField(blank=True,null=True)
    telephone = models.IntegerField(blank=True,null=True)
    extension =   models.IntegerField(blank=True,null=True)
    
    class Meta:
        ordering = ['identity', 'name' ,'department']
        
    def get_absolute_url(self):
         """Returns the url to access a particular author instance."""
         return reverse('ActivityUser-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'


class Venue(models.Model):
   # serial_number = models.CharField(max_length=10,primary_key=True)
    site_name =  models.CharField(max_length=12)
    activityuser = models.ForeignKey('ActivityUser', on_delete=models.SET_NULL, null=True, blank=True)
    area =  models.CharField(max_length=10)
    club_name = models.CharField(max_length=12)
    site_feature =  models.CharField(max_length=10)
    capacity =   models.IntegerField(blank=True,null=True)
    av_device =  models.CharField(max_length=40)
    suitable = models.CharField(max_length=40)
    photo = models.FileField
    venuemanager = models.ForeignKey('VenueManager', on_delete=models.SET_NULL, null=True, blank=True )
    
    def __str__(self):
        return self.site_name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('venue-detail', args=[str(self.id)]) 

class VenueManager(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, )
    extension =   models.IntegerField(blank=True,null=True)
    e_mail =  models.EmailField(blank=True,null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class VenueInstance(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole Venue')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, )
    venue = models.ForeignKey('Venue', on_delete=models.SET_NULL, null=True)
    activity_name = models.TextField(max_length=50)
    activity_attr =  models.CharField(max_length=10)
    activity_category =  models.CharField(max_length=10)
    activity_people = models.IntegerField(blank=True,null=True)
    activity_start = models.DateTimeField(null = True,blank=True)
    activity_end = models.DateTimeField(null = True,blank=True)
    meals_number =  models.IntegerField(blank=True,default=0)
    sound_control =  models.BooleanField(default=False)
    space_use =  models.CharField(max_length=10)
    user_service =  models.CharField(max_length=10)
    report =  models.BooleanField(default=False)
    message =  models.TextField(max_length=100,help_text=' 請輸入你的意見 ')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
    )
    
    class Meta:
        ordering = ['activity_start','activity_end']
        permissions = (("can_mark_returned", "Set venue as returned"),)
        
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.venue.site_name},{self.venue.club_name})'
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False