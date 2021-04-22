from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    #path('books/', views.BookListView.as_view(),name='books'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # path('authors/', views.AuthorListView.as_view(),name='authors'),
    # path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # path('book/<uuid:pk>/renew/', views.renew_book_librarian, name ='renew-book-librarian'),
    path('venues/', views.VenueListView.as_view(), name='venues'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue-detail'),
    path('activityusers/',views.ActivityUserListView.as_view(), name ='activityusers'),
    path('venueinstances/',views.VenueInstanceListView.as_view(), name = 'venueinstances'),
    path('myvenuess/', views.LoanedVenuesByUserListView.as_view(), name='my-borrowed'),
    path('add_venue', views.add_venue, name = 'add-venue'),
    path('add_venueinstance/',views.add_venueinstance, name = 'add-venueinstance'),
    path('<int:id>/', views.venueedit, name='venue-edit'),
    path('delete/<int:id>',views.venuedelete, name = 'venue-delete'),
]