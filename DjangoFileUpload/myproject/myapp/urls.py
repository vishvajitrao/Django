from django.urls import path
from . import views
from myapp.views import MyViews,AuthorCreate,AuthorDelete,AuthorUpdate


urlpatterns = [

    path('',views.Index, name='Index'),

    # Django upload file
    path('myapp',views.Home, name='Home'),
    path('myapps',views.CarsHome, name='CarsHome'),
    path('success',views.Success, name='Success'),
    path('upload',views.CustomUpload,name='CustomUpload'),
    path('docupload',views.Documents,name='Documents'),
    path('delete/<int:pk>',views.DeleteDocument,name='DeleteDocument'),

    #Register page
    path('register',views.Registration, name='Registration'),

    #Class based view
    path('cbview',MyViews.as_view(greeting = "G Day")),
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]
