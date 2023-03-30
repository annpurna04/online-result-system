"""faculty URL Configuration"""


from django.urls import path
from . import views


urlpatterns = [
    path('',views.faculty,name='faculty'),
    path('flogin',views.flogin,name='flogin'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('account',views.account,name='account'),
    path('create_account',views.create_account,name='create_account'),
    path('marks',views.marks,name='marks'),
    path('updated_marks',views.updated_marks,name='updated_marks'),
    path('chk_marks',views.chk_marks,name='chk_marks'),


]
