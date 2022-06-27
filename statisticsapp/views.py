from django.shortcuts import render
from rescueapp.models import Rescueclass
from .utils import get_plot
from .utils import get_barplot
from collections import Counter
# Create your views here.
def stats(request):
    qs=Rescueclass.objects.all()
    x=[x.animal for x in qs]
    cdog=0
    ccat=0
    cbird=0
    ccow=0
    for i in x:
        if i=='dog':
            cdog=cdog+1
        elif i=='cat':
            ccat=ccat+1
        elif i=='bird':
            cbird=cbird+1
        else:
            ccow=ccow+1
    chart=get_plot(cdog,ccat,cbird,ccow)
    
    y=[y.city for y in qs]
    d=Counter(y)
    lskey=[]
    lsvalue=[]
    '''
    d=dict()
    for i in y:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    
    for key in list(d.keys()):
        z=key
        if z not in lskey:
            lskey.append(z)
            lsvalue.append(d[key])
    '''

    lskey=d.keys()
    lsvalue=d.values()
    charts=get_barplot(lskey,lsvalue)  
        
        
    
    return render(request,'statistics.html',{'chart':chart,'charts':charts})