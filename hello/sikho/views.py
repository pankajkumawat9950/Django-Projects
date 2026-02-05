from django.shortcuts import render, HttpResponse
from datetime import datetime
from sikho.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"This is sent from views.py file"}
    return render(request, 'index.html')
    # return HttpResponse("this is Sikho App")
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is Sikho about page")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is Sikho Services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request, 'contact.html')
    # return HttpResponse("this is Sikho contact page")
def xz(request):
    return render(request, 'xz.html')
    # return HttpResponse("this is Sikho XZ page")