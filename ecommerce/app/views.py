from itertools import count
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . models import Product,Customer
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())


class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())  

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation! User Registration Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/customerregistration.html',locals())



class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html' ,locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']

            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,pincode=pincode)
            reg.save()
            messages.success(request,"Congratulations! Profile save Successfully")
        else:
            messages.warning(request,"Invalid Data")   

        return render(request, 'app/profile.html' ,locals())
    

def address(request):
    addr = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        form = CustomerProfileForm()
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        return render(request, 'app/updateAddress.html',locals())