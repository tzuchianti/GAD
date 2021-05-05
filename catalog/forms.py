from django import forms
from django.forms import ModelForm
from .models import Venue, VenueInstance, ActivityUser
import uuid
#from .widgets import XDSoftDateTimePickerInput
#create a venue form

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        exclude = ['activityuser']
        labels = {
            'site_name': '場地名稱',
            'activityuser' : '選擇活動申請人',
            'area': '地區',
            'club_name' : '會所名稱',
            'site_feature': '場地特性',
            'capacity' : '容納人數',
            'av_device' : '影音設備',    
            'suitable' : '適合活動',    
            'photo' : '場地照片',
            'venuemanager' : '選擇場地管理人',
        }
        widgets = {
            #'site_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder' : 'Site Name'}),
            'site_name': forms.TextInput(attrs = {'class':'form-control', }),
            'area' : forms.TextInput(attrs = {'class':'form-control', }),
            'club_name': forms.TextInput(attrs = {'class':'form-control', }),
            'site_feature' : forms.TextInput(attrs = {'class':'form-control', }),
            'capacity': forms.TextInput(attrs = {'class':'form-control', }),
            'av_device': forms.TextInput(attrs = {'class':'form-control', }),
            'suitable': forms.TextInput(attrs = {'class':'form-control', }),
        }

ACTIVITY_ATTR_CHOICES = [
    ('本會', '本會'),
    ('專案', '專案' )
]
ACTIVITY_CATEGORY_CHOICES = [
    ('會議，演講', '會議，演講'),
    ('研習，教學', '研習，教學' ),
    ('共修，集會', '共修，集會'),
]
#100-500 is question
ACTIVITY_PEOPLE_CHOICES = [
    ('100人以下', '100人以下'),
    ('100到500人', '100到500人'),
    ('500人以上', '500人以上'),
]
SOUND_CONTROL_CHOICES = [
    ('需要', '需要'),
    ('不需要', '不需要'),
]

class   VenueInstanceForm(ModelForm):
    class Meta:
        model = VenueInstance
        fields = "__all__"
        exclude = ['space_use', 'user_service', 'report', 'message', 'status', 'borrower']
        #field = ['id', 'venue', 'activity_start', 'activity_end', 'activity_name', 'activity_attr','activity_category', 'activity_people', 'meals_number', 'sound_control',]
        labels = {
            'id':'編號',
            'venue':'選擇場地',
            'activity_name':'活動名稱 ',
            'activity_attr':'活動屬性',
            'activity_category':'活動類別 ',
            'activity_people':'活動人數 ',
            'activity_start':'活動開始',
            'activity_end':'活動結束',
            'meals_number':'用餐人數',
            'sound_control':'音控志工',         
            'space_use':'空間使用滿意度',
            'user_service':'人員服務滿意度',
            'report':'是否回報',
            'message':'意見說明',
            'status':'場地狀態',               
        }
        widgets = {
            'activity_name':forms.TextInput(attrs={'class':'form-control', }),
            #'activity_attr':forms.TextInput(attrs={'class':'form-control', }),
            'activity_attr':forms.CheckboxSelectMultiple(choices=ACTIVITY_ATTR_CHOICES,),
            #'activity_category':forms.TextInput(attrs={'class':'form-control', }),
            'activity_category':forms.CheckboxSelectMultiple(choices=ACTIVITY_CATEGORY_CHOICES,),
            #'activity_people':forms.TextInput(attrs={'class':'form-control', }),
            'activity_people':forms.CheckboxSelectMultiple(choices=ACTIVITY_PEOPLE_CHOICES,),
            'activity_start':forms.TextInput(attrs={'class':'form-control',}),
            #'activity_start':forms.DateTimeInput(format='%d/%m%Y %H:%M', widget=XDSoftDateTimePickerInput()),
            'activity_end':forms.TextInput(attrs={'class':'form-control', }),
            'meals_number':forms.TextInput(attrs={'class':'form-control', }),
            #'sound_control':forms.TextInput(attrs={'class':'form-control', }),
            'sound_control':forms.CheckboxSelectMultiple(choices=SOUND_CONTROL_CHOICES,),
        }
        
class ActivityUserForm(ModelForm):
    class Meta:
        model = ActivityUser
        fields = "__all__"
        labels = {
            'identity':'身份別',
            'name':'姓名',
            'department':'部門',
            'e_mail':'信箱',
            'telephone':'電話',
            'extension':'雲端分機',
        }
        widgets = {
            'identity':forms.TextInput(attrs={'class':'form-control', }),
            'name':forms.TextInput(attrs={'class':'form-control', }),
            'department':forms.TextInput(attrs={'class':'form-control', }),
        }