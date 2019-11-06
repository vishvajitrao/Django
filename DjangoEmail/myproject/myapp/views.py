from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail,send_mass_mail,mail_admins,mail_managers
from django.core import mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.







    


def ContactMe(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipientss = []
            recipients  = form.cleaned_data['recipients']
            cc_myself = form.cleaned_data['cc_myself']

            sender = 'vishvajitrao@gmail.com'

            if cc_myself:
                recipientss.append(recipients) 

            send_mail(subject,message,sender,recipientss)
            return HttpResponse('<h1 style=text-align:center;>Thanks for using.. </h1>')
    # if this is a POST  mishra.abhi9619@gmail.com request we need to process the form data

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@login_required(login_url= '/login')
def SendEmail(request):
    sjt = "Jop opening"
    msg = "Immediate hiring for python developers"
    fromemail = "vishvajitrao12@gmail.com"
    toemail1 = ['vishvajitrao12@gmail.com']
    toemail2 = ['vishvajitrao@gmail.com']

    #send_mail(sjt,msg,fromemail,toemail,fail_silently=False)
    message1 = (sjt,msg,fromemail,toemail1)
    message2 = (sjt,msg,fromemail,toemail2)
    #send_mass_mail((message1,message2),fail_silently=False)
    #mail_admins(sjt,msg)  #Only send message for site admin
    #mail_managers(sjt,msg)
    return HttpResponse("<h1>Your email send successfully....</h1?")



def MyEmail(request):
    sjt = "Jop opening"
    bdy = "Immediate hiring for python developers"
    fromemail = "vishvajitrao12@gmail.com"
    with mail.get_connection() as connection:
        mail.EmailMessage(
            sjt,bdy,fromemail,['vishvajitrao@gmail.com','vishvajitrao12@gmail.com']
            
        ).send()
    return HttpResponse("<h1>Your email send successfully....</h1?")
        



def sendmyEmail(request):
    connection = mail.get_connection()
    sjt = "Jop opening"
    bdy = "Immediate hiring for python developers"
    fromemail = "vishvajitrao12@gmail.com"
    # Manually open the connection
    connection.open()


    # Construct an email message that uses the connection
    # email1 = mail.EmailMessage(
    #     sjt,bdy,fromemail,['vishvajitrao@gmail.com'],
    #     connection=connection,
    # )


    # email1.send() # Send the email



    #send two more message

    email2 = mail.EmailMessage(
        sjt,bdy,fromemail,['vishvajitrao@gmail.com'],
        
    )

    email3 = mail.EmailMessage(
        sjt,bdy,fromemail,['vishvajitrao12@gmail.com'],
        
    )

    # Send the two emails in a single call -
    connection.send_messages([email2, email3])
    #he connection was already open so send_messages() doesn't close it.
    # We need to manually close the connection.
    connection.close()
    return HttpResponse("<h1>Your email send successfully....</h1?")




def Index(request):
    return render(request,'base.html')




def Login(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username = username, password=  password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'homepage.html')
        else:
            return HttpResponse("Invalid login details..")
    else:
        return render(request,'login.html')



def Logout(request):
    logout(request)
    return redirect('/')


