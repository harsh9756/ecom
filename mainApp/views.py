from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth,messages
from django.contrib.auth.models import User 
from .models import *
# Create your views here.

def home(request):
    data=Product.objects.all()
    data=data[::-1]
    return render(request,'index.html',{"data":data})

def shop(request,mc,sc,brn):
    if(mc=='all' and sc=='all' and brn=='all'):
        data=Product.objects.all()

    elif(mc!='all' and sc=='all' and brn=='all'):
        data=Product.objects.filter(maincat=mainCategory.objects.get(name=mc))
    elif(mc=='all' and sc!='all' and brn=='all'):
        data=Product.objects.filter(subcat=subCategory.objects.get(name=sc))

    elif(mc=='all' and sc=='all' and brn!='all'):
        data=Product.objects.filter(brand=Brand.objects.get(name=brn))

    elif(mc!='all' and sc!='all' and brn=='all'):
        data=Product.objects.filter(maincat=mainCategory.objects.get(name=mc),
                                    subcat=subCategory.objects.get(name=sc))
        
    elif(mc!='all' and sc=='all' and brn!='all'):
        data=Product.objects.filter(maincat=mainCategory.objects.get(name=mc),
                                    brand=Brand.objects.get(name=brn))
            
    elif(mc=='all' and sc!='all' and brn!='all'):
        data=Product.objects.filter(subcat=subCategory.objects.get(name=sc),
                                    brand=Brand.objects.get(name=brn))    
    elif(mc!='all' and sc!='all' and brn!='all'):
        data=Product.objects.filter(maincat=mainCategory.objects.get(name=mc),
                                    subcat=subCategory.objects.get(name=sc),
                                    brand=Brand.objects.get(name=brn))
        

    mainCat=mainCategory.objects.all()
    subCat=subCategory.objects.all()
    br=Brand.objects.all()
    return render(request,"shop.html",{"data":data,
                                       "maincat":mainCat,
                                       'subcat':subCat,
                                       'brand':br,
                                       'mc':mc,
                                       'sc':sc,
                                       'brn':brn,
                                       })
def productPage(request,id):
    data=Product.objects.get(id=id)
    return render(request,'product.html',{'data':data})
def contact(request):
    return render(request,'contact.html')
def login(request):
    if(request.method == "POST"): 
        s=Seller()
        typee=request.POST.get('button')
        if (typee=="signup"):
            s.name=request.POST.get('name')
            s.email=request.POST.get('email')
            s.username=request.POST.get('username')
            pword=request.POST.get('password')
            confpword=request.POST.get('confpassword')
            s.phone=request.POST.get('phone')
            s.pin=request.POST.get('pin')
            s.city=request.POST.get('city')
            s.state=request.POST.get('state')
            print(pword,confpword)
            s.save()
            if(pword==confpword):
                user=User.objects.create_user(username=s.username,password=pword)
                user.set_password(pword)
                user.save()
                print(s.name,s.email,s.username,s.phone,s.pin,s.city,s.state)
            elif(confpword!=pword):
                messages.error(request,"Password Mismatch")
        elif(typee=='login'):
            pword=request.POST.get('password')
            s.username=request.POST.get('username')
            user=auth.authenticate(username=s.username,password=pword)
            if user is not None:
                auth.login(request,user)
                if(user.is_superuser):
                    return HttpResponseRedirect('/admin/')
                else:
                    return HttpResponseRedirect('/userprofile/')
            else:
                messages.error(request,("Invalid Username or Password. Try again..."))
        else:
            pass
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,"login.html")

def update(request):
    user=User.objects.get(username=request.user)
    seller=Seller.objects.get(username=request.user)
    if(request.method=='POST'):
        seller.name=request.POST.get("name")
        seller.email=request.POST.get("email")
        seller.phone=request.POST.get("phone")
        seller.city=request.POST.get("city")
        seller.state=request.POST.get("state")
        seller.pin=request.POST.get("pin")
        seller.save()
        return HttpResponseRedirect("/userprofile/")
    return render(request,'update.html',{'data':seller})

def userprofile(request):
    user=User.objects.get(username=request.user)
    seller=Seller.objects.get(username=request.user)
    return render(request,"userprofile.html",{"data":seller})
