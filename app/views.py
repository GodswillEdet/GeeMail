from django.shortcuts import render

def send_email(request):
    return render(request, 'index.html')

def sent_email(request):
    return render(request, 'success.html')