from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm



def login_user(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main_page')
		else:
			messages.success(request,("Verify your login info !"))
			return redirect('login')
	else:
		return render(request,'authenticate/login.html',{})	

def logout_user(request):
	logout(request)
	return redirect('main_page')

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('main_page')
	else:
		form = RegisterUserForm()
	return render(request, 'authenticate/register_user.html', {'form':form})

