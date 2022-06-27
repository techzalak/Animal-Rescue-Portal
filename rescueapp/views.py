from django.shortcuts import render,HttpResponseRedirect
from .forms import RescueDetails
from .models import Rescueclass
from workwithus.models import Signupclass 
from .models import Message
from django.contrib import messages
# Create your views here.

def showformdata(request):
    #lastimage= Rescueclass.objects.last()
    #img=lastimage.img
    if(request.method == 'POST'):
        fm = RescueDetails(request.POST, request.FILES)
        if(fm.is_valid()):
            nm = fm.cleaned_data['name']
            mm = fm.cleaned_data['mobile']
            am = fm.cleaned_data['animal']
            im = fm.cleaned_data['img']
            sm = fm.cleaned_data['strt']
            lm = fm.cleaned_data['lama']
            cm = (fm.cleaned_data['city']).lower()
            pm = fm.cleaned_data['pin']
            rreg = Rescueclass(name=nm,  mobile=mm, animal=am, img = im, strt=sm, lama=lm, city=cm, state=sm, pin=pm)
            rreg.save()
            users=Signupclass.objects.filter(pin=pm)
            if users.exists():
                for use in users:
                    print(use.user)
                    vol=use.user
                    msg="There is a " + am +" in need of rescue at :-" +lm+","+sm+","+cm+" - "+pm+"   Help-seeker:"+nm+" , "+mm
                    mreg=Message(user=vol,msg=msg)
                    mreg.save()
                    messages.add_message(request, messages.SUCCESS, 'Thank you for registering this issue. Help will be provided as fast as possible')
            else:
                messages.add_message(request, messages.INFO, 'Sorry volunteer is not available in your area')
            return HttpResponseRedirect('/rescue/')
            

    else:
        fm = RescueDetails()
    return render(request,'rescuepage.html', {'form': fm})