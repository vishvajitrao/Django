from django.urls import path
from . import views


urlpatterns  = [
    path('',views.Index, name='Index'),
    path('contact-us',views.ContactMe, name='ContactMe'),
    path('sendmail',views.SendEmail, name='SendEmail'),
    path('emailsend',views.MyEmail, name='MyEmail'),
    path('emailsends',views.sendmyEmail, name='sendmyEmail'),
    path('login',views.Login, name='Login'),
    path('logout',views.Logout, name='Logout'),
]