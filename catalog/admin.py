from django.contrib import admin
from .models import ActivityUser,Venue,VenueManager,VenueInstance
from import_export.admin import ImportExportModelAdmin
from import_export import resources
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


#admin control import export
class VenueInstanceResource(resources.ModelResource):
    class Meta:
        model = VenueInstance
        export_order = ('id', 'venue', 'activity_name', 'activity_attr', 'activity_category', 'activity_people', 'activity_start', 'activity_end', 'meals_number', 'sound_control', )


@admin.register(VenueInstance)
#class VenueInstanceAdmin(admin.ModelAdmin):
class VenueInstanceAdmin(ImportExportModelAdmin):
    list_display = ('venue', 'status', 'borrower', 'activity_start', 'activity_end', 'id')
    list_filter = ('status', 'activity_start', 'activity_end',)
    resource_class = VenueInstanceResource
    fieldsets = (
        (None,{
            'fields':('venue', 'id')
        }),
        ('Availability', {
            'fields':('status', 'borrower', 'activity_name', 'activity_attr', 'activity_category', 'activity_people', 'meals_number', 'activity_start', 'activity_end', )
        }),
    )

# class VenueInstanceAdmin(ImportExportModelAdmin):
#     resource_class =VenueInstanceResource