from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):

	if request.method == 'POST':
		password= request.POST.get('password1','')
		email = request.POST.get('username','')
		print(email)
		user = auth.authenticate(username = email,password = password);

		if user is not None:
			auth.login(request,user);
			return redirect('/')
		else:
			messages.info(request,"invalid user.....")
			return redirect('login')

	else:
 		return render(request,'login.html')
def register(request):

	if request.method == 'POST':
		firstname = request.POST.get('firstname','')
		lastname = request.POST.get('lastname','')
		username = request.POST.get('username')
		password1 = request.POST.get('password1','')
		password2 = request.POST.get('password2','')
		email = request.POST.get('email','')
		if password1==password2:
			if User.objects.filter(email = email).exists():
				messages.info(request,"Email is already used.....")
				return redirect('register')
			else:
				user = User.objects.create_user(username = username,password = password1,email = email,first_name = firstname, last_name = lastname);
				user.save()
				return redirect('login')
		else:
			messages.info(request,"password is not matched")
		return redirect('/');

	else:
 		return render(request,'register.html')

def logout(request):
 	auth.logout(request);
 	return redirect('/')