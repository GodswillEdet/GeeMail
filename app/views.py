import imp
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def send_email(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message') 
        email_from = request.POST.get('email')
        recipient_list = request.POST.get('email')
        
        print(subject, message, email_from, recipient_list)
        return redirect('sent')
    return render(request, 'index.html')

def sent_email(request):
    return render(request, 'success.html')