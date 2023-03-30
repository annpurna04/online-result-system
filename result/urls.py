"""result URL Configuration"""


from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_header= "Online Result System"
admin.site.site_title= "Online Result System"
admin.site.index_title= "Online Result Site"

urlpatterns = [
    path('', views.index,name='index'),
    path('student/',include('student.urls')),    
    path('faculty/',include('faculty.urls')),


    path('admin/', admin.site.urls),
]
