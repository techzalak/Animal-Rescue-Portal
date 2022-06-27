from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Signupclass
from django.contrib import messages
from rescueapp.models import Message
#from .forms import Login
from .forms import sign, Edit, addEdit, Address
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.
def work1(request):
    if request.method == 'POST':
        if request.POST.get('SignUp'): #if SignUp button is clicked
            
            fm=sign(request.POST, prefix="fm")
            form1=AuthenticationForm(prefix= "form1") 
            if fm.is_valid(): 
                user=fm.save()
                mm=fm.cleaned_data['mobile']
                ad=fm.cleaned_data['address']
                wreg =Signupclass(mobile=mm, address=ad,user=user)
                wreg.save()
                messages.add_message(request, messages.SUCCESS, 'Account created sucessfully stored successfully')
      
        
        elif request.POST.get('Login'): #if Login button is clicked
    

            form1=AuthenticationForm(request=request, data=request.POST, prefix= "form1") 
            fm=sign(prefix="fm") 

            if form1.is_valid():
                uname=form1.cleaned_data['username']
                upass=form1.cleaned_data['password']
                au=authenticate(username=uname,password=upass)
                if au is not None:
                    login(request, au)
                    return HttpResponseRedirect('/workwithus/profile/')
           
    else:
        form1 = AuthenticationForm(prefix="form1") 
        
        fm=sign(prefix="fm")
        
    return render(request,'workwithus.html',{'form1':form1,'fm': fm})

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('save'):         #if save button of edit profile is clicked
                uedit = Edit(request.POST,instance=request.user,prefix="uedit")
                use = Signupclass.objects.get(user=request.user)    #getting fields corresponding to current username from signup class
                adedit = addEdit(request.POST, instance=use,prefix="adedit")
                if(use.strt=="None" or use.lama=="None" or use.state=="None" or use.city=="None" or use.pin=="None"): #if address is not filled return blank form
                    addr=Address(prefix="addr")
                else:
                    addr= Address(instance=use,prefix="addr") #else return filled form
                if uedit.is_valid() and adedit.is_valid():
                    um=uedit.save()
                    use.user = um
                    use.address = adedit.cleaned_data['address']
                    use.mobile = adedit.cleaned_data['mobile']
                    use.save()
                    return HttpResponseRedirect('/workwithus/profile/')
            elif request.POST.get('address'):   #if save button of address is clicked
                uedit = Edit(instance=request.user,prefix="uedit")
                use = Signupclass.objects.get(user=request.user)
                adedit = addEdit(instance=use,prefix="adedit")
                addr= Address(request.POST,instance=use,prefix="addr")
                if(addr.is_valid()):
                    use.strt = addr.cleaned_data['strt']
                    use.lama = addr.cleaned_data['lama']
                    use.city = addr.cleaned_data['city']
                    use.pin = addr.cleaned_data['pin']
                    use.state = addr.cleaned_data['state']
                    use.save()
                    return HttpResponseRedirect('/workwithus/profile/')
        else:        
            uedit = Edit(instance=request.user,prefix="uedit")
            use = Signupclass.objects.get(user=request.user)
            adedit = addEdit(instance=use,prefix="adedit")
            per=Message.objects.filter(user=request.user).order_by('-id') #retrieve notifications of current user
            if per.exists():
                pp1=per.all()[0]
                pp2=per.all()[1:]
            else:
                pp1='none'
                pp2='none'
            if(use.strt=="None" or use.lama=="None" or use.state=="None" or use.city=="None" or use.pin=="None"):
                addr=Address(prefix="addr")
            else:
                addr= Address(instance=use,prefix="addr")
        return render(request,'account.html',{'name': request.user,'uedit': uedit,'adedit': adedit,'addr':addr,'pp1':pp1,'pp2':pp2})
    else:
        return HttpResponseRedirect('/workwithus/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/workwithus/')