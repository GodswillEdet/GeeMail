import imp
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')

def send_email(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message') 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = request.POST.get('email')
        
        print(subject, message, email_from, recipient_list)
        send_mail( subject, message, email_from, recipient_list )
    return redirect('sent')
    
def sent(request):
    return render(request, 'success.html')



