from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, Addclient,saveinvoice,product,saveuserpayment, saveusercompany,number1,product1
from .models import profile, register,client, Invoice,Usercompany,Userpayment,Product,Number,Product1
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            new_user=user
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/userprofile.html', {'new_user': new_user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login1.html', {'form': form})


def dashboard(request):
    form = LoginForm()
    return render(request,
                  'account/login1.html',
                  {'form': form})
def forget(request):
    return render(request,
                  'account/forget.html',
                  )
@login_required
def usercompany(request):
    return render(request,
                  'account/usercompany.html',
                  )
@login_required
def userprofile(request):
    return render(request,
                  'account/userprofile.html',
                  )
@login_required
def userpayment(request):
    return render(request,
                  'account/userpayment.html',
                  )

@login_required
def clientdashboard(request):
    return render(request,
                  'account/clientdashboard.html',
                  )


@login_required
def invoicedashboard(request):
    a=Invoice.objects.all()
    return render(request,
                          'account/invoicedashboard.html',
                          {'new_user': a})
    
@login_required
def goodsdashboard(request):
  
    return render(request,
                          'account/goodsdashboard.html',
                          )
@login_required
def addgoods(request):
  
    return render(request,
                          'account/addgoods.html',
                          )
#def addinvoice(request):
  #  Product.objects.all().delete()
       
  #  return render(request,
   #               'account/addinvoice.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/userprofile.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
@login_required
def saveusercompany1(request):
    if request.method == 'POST':
        user_form = saveusercompany(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            # Save the User object
            new_user.save()
            return render(request,
                          'account/usercompany.html',
                          {'new_user': new_user})
    else:
        user_form = saveusercompany()
    return render(request,
                  'account/usercompany.html',
                  {'user_form': user_form})
@login_required
def saveuserpayment1(request):
    if request.method == 'POST':
        user_form = saveuserpayment(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            # Save the User object
            new_user.save()
            return render(request,
                          'account/userpayment.html',
                          {'new_user': new_user})
    else:
        user_form = saveuserpayment()
    return render(request,
                  'account/userpayment.html',
                  {'user_form': user_form})
@login_required
def saveclient(request):
    if request.method == 'POST':
        user_form = Addclient(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request,
                          'account/clientdashboard.html',
                          {'new_user': new_user})
    else:
        user_form = Addclient()
    return render(request,
                  'account/addclient.html',
                  {'user_form': user_form})
@login_required
def saveinvoice1(request):
    if request.method == 'POST':
        user_form = saveinvoice(request.POST)
        user_form2 = Addclient(request.POST)
        #user_form3= number1(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_user.save()
            #new_user3 = user_form3.save(commit=False)
            #new_user3.quan=new_user1.id
            #new_user3.save()
            a=Invoice.objects.all()
            #user_form1 = product()
            return render(request,
                          'account/invoicedashboard.html',
                          {'new_user': a})
    else:
        user_form = saveinvoice()
        user_form1 = product()
        user_form2 = Addclient()
        p=Product1.objects.all()
        p1=Product.objects.all()
    return render(request,
                  'account/Addinvoice.html',
                  {'user_form': user_form,
                   'user_form1': user_form1,
                   'user_form2': user_form2,
                   'p':p,'p1':p1
                   })
@login_required
def saveproduct(request):
    if request.method == 'POST':
        
        user_form1 = product(request.POST)
      
        #user_form3= number1(request.POST)
        if user_form1.is_valid:
            # Create a new user object but avoid saving it yet
           
            new_user1 = user_form1.save(commit=False)
            c=(new_user1.price*new_user1.quantity)*(1+new_user1.vat/100)
            new_user1.subtotal=new_user1.quantity*new_user1.price
            new_user1.tax=(new_user1.vat*new_user1.quantity*new_user1.price)/100
            new_user1.totalprice=c
            new_user1.sumprice=new_user1.subtotal+ new_user1.sumprice
            new_user1.sumtax=new_user1.tax+ new_user1.sumtax
            new_user1.sumtotal=new_user1.totalprice+ new_user1.sumtotal
            new_user1.save()
            #new_user3 = user_form3.save(commit=False)
            #new_user3.quan=new_user1.id
            #new_user3.save()
            a=Invoice.objects.all()
            #user_form1 = product()
            return render(request,
                          'account/invoicedashboard.html',
                          {'new_user': a})
    else:
        user_form = saveinvoice()
        user_form1 = product()
        user_form2 = Addclient()
        p=Product1.objects.all()
        p1=Product.objects.all()
    return render(request,
                  'account/Addinvoice.html',
                  {'user_form': user_form,
                   'user_form1': user_form1,
                   'user_form2': user_form2,
                   'p':p,'p1':p1
                   })
@login_required
def savegoods(request):
    if request.method == 'POST':
       
        user_form1 = product1(request.POST)
       
        if  user_form1.is_valid:
            # Create a new user object but avoid saving it yet         
            new_user1 = user_form1.save(commit=False)
            new_user1.save()
                  
            return render(request,
                          'account/goodsdashboard.html',
                          )
    else:
        
        user_form1 = product1()
      
    return render(request,
                  'account/addgoods.html',
                  {
                   'user_form1': user_form1}
                   )
@login_required
def render_pdf_view(request,id):
    a=get_object_or_404(Invoice, id=id)
    b=Usercompany.objects.last()
    c=Userpayment.objects.last()
    d2=Product.objects.all()
    d=Product.objects.all()
    dd=Product.objects.all()
    ddd=Product.objects.all()
    d1=0
    d3=d4=0
    for d in d:
         d1=d1+d.sumprice
    for d in dd:
         d3=d3+d.sumtax
    for d in ddd:
         d4=d4+d.sumtotal
    template_path = 'pdf.html'
    context = {'a': a,'b':b,'c':c,'d2':d2,'d1':d1,'d3':d3,'d4':d4}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
   
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
 
    return response
