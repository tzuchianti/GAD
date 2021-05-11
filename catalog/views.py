from django.shortcuts import render,redirect
from django.views import generic
from datetime import datetime
from .models import ActivityUser,Venue,VenueManager,VenueInstance
from .forms import VenueForm,VenueInstanceForm, ActivityUserForm
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import  permission_required
import uuid

import logging
logger = logging.getLogger('django')

@permission_required('catalog.can_mark_returned')
@permission_required('catalog.can_edit')
def  my_view(request):
   pass




class LoanedVenuesByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = VenueInstance
    template_name ='catalog/venueinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return VenueInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('activity_end')
# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'


class IndexListView(generic.ListView):
    model = Venue
    paginate_by = 20
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='Game')[:4] # Get 5 books containing the title war
    template_name = 'index.html'  # Specify your own template name/location

def venues(request):
    """View function for home page of site."""

    #get currnet year
    now = datetime.now()
    current_year = now.year
    # Generate counts of some of the main objects
    num_venues = Venue.objects.all().count()
    num_instances = VenueInstance.objects.all().count()
    
    users_list = ActivityUser.objects.all()
    venues = Venue.objects.all().order_by('-id')
    
    # Available books (status = 'a')
    num_instances_available = VenueInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_activityusers = ActivityUser.objects.count()
    
    #Number of visits to this view , as counted in the session variable.
    num_visists = request.session.get('num_visits' ,0)
    request.session['num_visits'] = num_visists + 1
    
    context = {
        'num_venues': num_venues,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_activityusers': num_activityusers,
        'num_visits' : num_visists,
        'venues':venues,
        'current_year':current_year,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/venue_list.html', context=context)
    #return render(request, 'index.html', {'venues':venues, 'current_year':current_year,})

def analysis(request):
    return HttpResponse("統計分析")

class VenueDetailView(generic.DetailView):
    model = Venue
    
# class ActivityUserListView(generic.ListView):
#     model = ActivityUser
#     template_name = 'activityusers/activityuser_list.html' 
 
def activityusers_list(request):
    activityusers = ActivityUser.objects.all().order_by('-id')
    return render(request, 'catalog/activityusers_list.html', {'activityusers':activityusers})

     
# class VenueInstanceListView(generic.ListView):
#     model = VenueInstance
#     venueinstances = VenueInstance.objects.all().order_by('activity_start')
#     template_name = 'VenueInstances/venueinstance_list.html' 
    
def venueinstances_list(request):
    venueinstances = VenueInstance.objects.all()
    context = {
        'venueinstances':venueinstances
    }
    return render(request, 'catalog/venueinstances_list.html', context=context)

########################ADD######################   
# VenueForm setting
def add_venue(request):
    submitted = False
    if request.method == "POST" :
        form = VenueForm(request.POST)
        if form .is_valid():
            form.save()
            return HttpResponseRedirect('/catalog/add_venue?submitted=True')
    else:
            form = VenueForm
            if 'submitted' in request.GET:
                submitted = True
            return render(request, 'catalog/add_venue.html', {'form':form, 'submitted':submitted})

def add_activityuser(request):
    submitted = False
    if request.method == "POST" :
        form = ActivityUserForm(request.POST)
        if form .is_valid():
            form.save()
            return HttpResponseRedirect('/catalog/add_activityuser?submitted=True')
    else:
            form = ActivityUserForm
            if 'submitted' in request.GET:
                submitted = True
            return render(request, 'catalog/add_activityuser.html', {'form':form, 'submitted':submitted})

#venueinstanceform  setting 
# 日期輸入格式不正確，網頁會顯示錯誤
def  add_venueinstance(request):
    submitted = False
    if request.method == "POST" :
        form = VenueInstanceForm(request.POST)
        if form .is_valid():
            form.save()
            return HttpResponseRedirect('/catalog/add_venueinstance?submitted=True')
    else:
            form = VenueInstanceForm
            if 'submitted' in request.GET:
                submitted = True
            return render(request, 'catalog/add_venueinstance.html', {'form':form, 'submitted':submitted})



####################EDIT#########################
def venueedit(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = VenueForm()
        else:
            venue = Venue.objects.get(pk = id)
            form =  VenueForm(instance = venue)
        return render(request, "catalog/venue_update.html", {'form':form})
    else:
        if id ==0:
            form = VenueForm(request.POST)
        else:
            venue = Venue.objects.get(pk = id)
            form = VenueForm(request.POST, instance = venue)
        if form.is_valid():
            form.save()
        return redirect('venues')

def activityuseredit(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = ActivityUserForm()
        else:
            activityuser = ActivityUser.objects.get(pk = id)
            form =  ActivityUserForm(instance = activityuser)
        return render(request, "catalog/activityuser_update.html", {'form':form})
    else:
        if id ==0:
            form = ActivityUserForm(request.POST)
        else:
            activityuser = ActivityUser.objects.get(pk = id)
            form =  ActivityUserForm(request.POST, instance = activityuser)
        if form.is_valid():
            form.save()
        return redirect('activityusers-list')

def venueinstanceedit(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = VenueInstanceForm()
        else:
            venueinstance = VenueInstance.objects.get(pk = id)
            form =  VenueInstanceForm(instance = venueinstance)
        return render(request, "catalog/venueinstance_update.html", {'form':form})
    else:
        if id ==0:
            form = VenueInstanceForm(request.POST)
        else:
            venueinstance = VenueInstance.objects.get(pk = id)
            form = VenueInstanceForm(request.POST, instance = venueinstance)
        if form.is_valid():
            form.save()
        return redirect('venueinstances-list')

##########report####################
def venueinstancereport(request):
    return HttpResponse("回報成功")


##############Delete################
def venuedelete(request, id):
    venue = Venue.objects.get(pk = id)
    venue.delete()
    return redirect('venues')

def activityuserdelete(request, id):
    activityuser = ActivityUser.objects.get(pk = id)
    activityuser.delete()
    return redirect('activityusers-list')

def venueinstancedelete(request, id):
    venueinstance = VenueInstance.objects.get(pk = id)
    venueinstance.delete()
    return redirect('venueinstances-list')



 