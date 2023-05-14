from django.shortcuts import render, redirect
from .models import *
from Home.models import Products
from .models import Item
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def home(request):
    prop = Products.objects.all()
    return render(request, 'home.html', {'prop':prop})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def video(request):
    object=Item.objects.all()
    return render(request, 'video.html', {'object': object})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("Home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})




    
