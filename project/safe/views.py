from django.shortcuts import render,redirect
from .models import PassStore
from cryptography.fernet import Fernet
from passwordsafe.settings import PASS_KEY
from django.http import JsonResponse

def home(request):
    return render(request,'safe/home.html')

def userpage(request):
    if request.method=='POST':
        site=request.POST['website']
        username=request.POST['username']
        sitepass=request.POST['password']
        f=Fernet(PASS_KEY)
        sitepass=f.encrypt(bytes(sitepass,'utf-8'))
        PassStore.objects.create(user=request.user,username=username,website=site,password=sitepass.decode('utf-8'))
        return redirect('safe:userpage')
        #encrypt the pass and save to db
    else:
        qs=PassStore.objects.filter(user=request.user)
    return render(request,'safe/userpage.html',{'objects':qs})

def decrypt(request,id):
    object=PassStore.objects.get(id=id)
    return JsonResponse({'pass':object.conv()})

def encrypt(request,password):
    f=Fernet(PASS_KEY)
    sitepass=f.encrypt(bytes(password,'utf-8'))
    sitepass=sitepass.decode('utf-8')
    return JsonResponse({'password':sitepass})
