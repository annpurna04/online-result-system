"""student URL Configuration"""


from django.urls import path
from . import views


urlpatterns = [
    path('',views.student,name="student"),
    path('slogin',views.slogin,name="slogin"),
    path('shome',views.shome,name="shome"),
    path('smarks',views.smarks,name="smarks"),
    path('slogout',views.slogout,name="slogout"),
    

]
