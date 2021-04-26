from django.urls import path
from . import views

urlpatterns = [
     path('',views.IndexListView.as_view(),name='index'),
     path('venues/', views.venues, name='venues'),
    # path('',views.index,name='index'),
    # path('venues/', views.VenueListView.as_view(), name='venues'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue-detail'),
    path('activityusers_list', views.activityusers_list, name = 'activityusers-list'),
    #path('activityusers/',views.ActivityUserListView.as_view(), name ='activityusers'),
    path('venueinstances_list', views.venueinstances_list, name='venueinstances-list'),
    #path('venueinstances/',views.VenueInstanceListView.as_view(), name = 'venueinstances'),
    path('myvenuess/', views.LoanedVenuesByUserListView.as_view(), name='my-borrowed'),
    path('add_venue', views.add_venue, name = 'add-venue'),
    path('add_venueinstance/',views.add_venueinstance, name = 'add-venueinstance'),
    path('<int:id>/', views.venueedit, name='venue-edit'),
    path('delete/<int:id>',views.venuedelete, name = 'venue-delete'),
]