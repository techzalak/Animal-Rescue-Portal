from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import donateform
from .models import Donateclass
from django.conf import settings
import stripe

# Create your views here.
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

def support(request):
    return render(request,'supportus.html')
def donate(request):
    if(request.method== 'POST'):
            amt=request.POST['amt']
            fm = donateform(request.POST,prefix='fm')
            
            if fm.is_valid():
                nm=fm.cleaned_data['name']
                em=fm.cleaned_data['email']
                mm=fm.cleaned_data['mobile']
                cm=fm.cleaned_data['comment']
                ad=fm.cleaned_data['add']
                #st=fm.cleaned_data['state']
                an=fm.cleaned_data['anony']
                #dreg=Donateclass(name=nm,email=em,mobile=mm,comment=cm,add=ad,anony=an,amt=amt)
                #dreg.save()
                #cred=creditform()
                dreg=Donateclass(name=nm,email=em,mobile=mm,comment=cm,add=ad,anony=an,amt=amt)
                dreg.save()
                return HttpResponseRedirect("/supportus/payment/")
    else:
        fm = donateform(prefix='fm')
    od = Donateclass.objects.order_by('-id')
    don = od.all()[:5]
    #don = Donateclass.objects.reverse()[:3]
    don2 =od.all()[5:]
    
    return render(request,'donate.html',{'form':fm , 'don': don, 'don2': don2})


class pay(TemplateView):
    template_name='payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']            
        )
    return render(request, 'charge.html')