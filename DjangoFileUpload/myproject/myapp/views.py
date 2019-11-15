from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import ProfileUpload, MyDetails
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from myapp.models import Author
from django.core.files.storage import FileSystemStorage


# Create your views here.


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg','pdf','txt','ico']

def Index(request):
    return render(request, 'index.html')


# upload file using file type using list
def Home(request):
    if request.method == 'POST':
        form = ProfileImage(request.POST,request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            print(fm)
            fm.Profile = request.FILES['Profile']
            print(fm.Profile.url)
            file_type = fm.Profile.url.split('.')[-1]
            print(file_type)
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse("Invalid file")
            else:
                fm.save()
                return HttpResponseRedirect('/success')        
    else:
        form = ProfileImage()
    return render(request, 'home.html',{'form':form})


#Upload multiple file on same time
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def CarsHome(request):
    cars = Cars.objects.all()
    if request.method == 'POST':
        form = CarUploadForm(request.POST,request.FILES)
        mycars = request.FILES.getlist('cars')
        print(mycars)
        if form.is_valid():
            form.save()     
            for c in mycars:
                cars = Cars(cars = c)
                cars.save()         
            return HttpResponseRedirect('/myapps')
        
    else:
        form = CarUploadForm()
        return render(request, 'cars.html',{'form':form,'cars':cars})


#Upload documents 
def Documents(request):
    istrue = True
    docs = Document.objects.all()
    print(type(docs))
    if request.method == 'POST':
        form = DocumentUpload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/docupload")
    else:
        form = DocumentUpload()

    return render(request,'home.html',{'docform':form,'docs':docs,'istrue':istrue})

#Delete uploaded document

def DeleteDocument(request,pk):
    doc = Document.objects.get(pk = pk)
    doc.delete()
    return HttpResponseRedirect('/docupload')
    
    

# success after 
def Success(request):
    myimage = ProfileUpload.objects.all()  
    return render(request,'success.html',{'myimage':myimage})

def Registration(request):
    return render(request, 'register.html')


#Upload file without model using FileStorageClass 
def CustomUpload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']

        #FileSystemStorage object - fs
        fs = FileSystemStorage()
        name= fs.save(upload_file.name,upload_file)

        # Print some detail of file using FileSystemStorage object and mothods
        print(fs.exists(upload_file.name)) 
        print(fs.get_accessed_time(upload_file.name)) 
        print(fs.get_available_name(upload_file.name))
        print(fs.get_created_time(upload_file.name))
        print(fs.get_modified_time(upload_file.name))
        print(fs.get_valid_name(upload_file.name))
        print(fs.size(upload_file.name))
        print(fs.path(upload_file.name))
        print(fs.url(upload_file.name))
        # print(fs.delete(upload_file.name)) 
        print(fs.exists(upload_file.name)) 
        

        #Print some details of file
        print(upload_file.name)
        print(upload_file.size)
        print(upload_file.file)     
        context['urls'] = fs.url(name)
        return HttpResponseRedirect("/upload")
    return render(request,'home.html',context)



# Class Based views 


from django.views import View
class MyViews(View):
    greeting = "Good Day"
    def get(self,request):
        return HttpResponse(self.greeting)



class AuthorCreate(CreateView):
    model  = Author
    fields = ['name']



class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    template_name_suffix = '_update_form'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('Registration')



