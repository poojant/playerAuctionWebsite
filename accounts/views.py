from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import teamForm
from accounts.models import team1, PlayerImage
from django.contrib.auth import logout

# Create your views here.

#def home(request):
#	return render(request, 'login.html')

def startAuction(request):
	
	players = ["Virat","Rohit","Dhoni","Raina","Hardik"]
	form = teamForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			pname = request.POST.get('pname', '')
			tname = int(request.POST.get('tname', ''))
			pnum = int(request.POST.get('pnum', ''))
			obj = team1(name = pname)
			obj.save()
			if pnum == 5:
				return redirect('http://127.0.0.1:8000/accounts/teamdisplay')
			else:
				args = {'pname': players[pnum], 'pnum': pnum}
				return redirect('/accounts/auction?pnum='+str(pnum))
			#messages.success(request, 'Account created successfully')
			#args = {'pname': players[pnum]}
			#return redirect('http://127.0.0.1:8000/accounts/login')
		else:
			form = teamForm()
	else:
		pnum_get = request.GET.get('pnum')
		if pnum_get is not None and pnum_get != '':
			args = {'form': form, 'pname': players[int(pnum_get)], 'pnum': pnum_get}
		else:
			args = {'form': form, 'pname': players[0]}
		
		return render(request, 'auction.html', args)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#messages.success(request, 'Account created successfully')
			return redirect('http://127.0.0.1:8000/accounts/login')
	else:
		form = UserCreationForm()

	args = {'form': form}
	return render(request, 'reg_form.html', args)

def displayTeam(request):
	
	names = team1.objects.all()
	args = {'pnames' : names}
	return render(request, 'teamdisplay.html', args)

def imageGallery(request):
	img = PlayerImage.objects.all()
	args = {'image' : img}
	print(img[0].img)
	return render(request, 'imagegallery.html', args)
#def logoutView(request):
#	logout(request)
#	username = request.GET.get('username')
#	args = {'username': username}
#	return render(request, 'logout.html', args)