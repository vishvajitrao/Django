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

    #Django session 
    path('testcookie',views.session_cookie, name='session_cookie'),
    path('checkcookie',views.check_cookie, name='check_cookie'),
    path('deletecookie',views.delete_cookie, name='delete_cookie'),


    #create and accessing Django session

    path('create',views.create_session,name='create_session'),
    path('access',views.access_session,name='access_session'),
    path('check',views.check_session,name='check_session'),
    path('delete',views.delete_session,name='delete_session'),

]