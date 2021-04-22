from django.contrib import admin
from .models import ActivityUser,Venue,VenueManager,VenueInstance
# Register your models here.

#admin.site.register(ActivityUser)
admin.site.register(VenueManager)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('site_name' , 'area' , 'club_name', 'site_feature' , )
    
admin.site.register(Venue, VenueAdmin)


class ActivityUserAdmin(admin.ModelAdmin):
    list_display = ('identity','name','department','extension',)
    fields =['identity', 'name', 'department', 'e_mail', 'telephone', 'extension']
    
#Register the admin class with the associated model
admin.site.register(ActivityUser, ActivityUserAdmin)


@admin.register(VenueInstance)
class VenueInstanceAdmin(admin.ModelAdmin):
    list_display = ('venue', 'status', 'borrower', 'activity_start', 'activity_end', 'id')
    list_filter = ('status', 'activity_start', 'activity_end',)
    
    fieldsets = (
        (None,{
            'fields':('venue', 'id')
        }),
        ('Availability', {
            'fields':('status', 'borrower', 'activity_name', 'activity_attr', 'activity_category', 'activity_people', 'meals_number', 'activity_start', 'activity_end', )
        }),
    )
