from django.shortcuts import render,redirect
from django.views import generic
from datetime import datetime
from .models import ActivityUser,Venue,VenueManager,VenueInstance
from .forms import VenueForm,VenueInstanceForm
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import  permission_required


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


# class VenueListView(generic.ListView):
#     model = Venue
#     paginate_by = 20
#     #context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     #queryset = Book.objects.filter(title__icontains='Game')[:4] # Get 5 books containing the title war
#     template_name = 'venues/venue_list.html'  # Specify your own template name/location
    

class VenueDetailView(generic.DetailView):
    model = Venue
    
class ActivityUserListView(generic.ListView):
    model = ActivityUser
    template_name = 'activityusers/activityuser_list.html' 
    
class VenueInstanceListView(generic.ListView):
    model = VenueInstance
    venueinstances = VenueInstance.objects.all().order_by('activity_start')
    template_name = 'VenueInstances/venueinstance_list.html' 
    
    
# Forms setting
def  add_venue(request):
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


def venueedit(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = VenueForm()
        else:
            venue = Venue.objects.get(pk = id)
            form =  VenueForm(instance = venue)
        return render(request, "/catalog/venue_update.html",{'form':form})
    else:
        if id ==0:
            form = VenueForm(request.POST)
        else:
            venue = Venue.objects.get(pk = id)
            form = VenueForm(request.POST, instance = venue)
        if form.is_valid():
            form.save()
        return redirect('venues')

    
def venuedelete(request, id):
    venue = Venue.objects.get(pk = id)
    venue.delete()
    return redirect('venues')
  

# def delete(request,id=None):  #刪除資料
# 	if id!=None:
# 		if request.method == "POST":  #如果是以POST方式才處理
# 			id=request.POST['venue_id'] #取得表單輸入的編號
# 		try:
# 			unit = Venue.objects.get(id=id)  
# 			unit.delete()
# 			return redirect('/index/')
# 		except:
# 			message = "讀取錯誤!"			
# 	return render(request, "venue_delete.html", locals())

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


 