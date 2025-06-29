from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect

from companyapp.models import FAQ, About, Contactform, Generalsetting, Portfolio, Service, Slider, Team # type: ignore

# Create your views here.
def homefunction(request):
    sliders = Slider.objects.all()
    about = About.objects.get(id=1)
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    teams = Team.objects.all()
    faqs = FAQ.objects.all()
    generalsetting = Generalsetting.objects.get(id=1)
      
    context = {
        'sliders' : sliders,
        'about' : about,
        'services' : services,
        'portfolios' : portfolios,
        'teams' : teams,
        'faqs' : faqs,
        'generalsetting' : generalsetting,   
    }
    return render(request, 'companyapp/index.html',context)



def portfolio_detail(request,pk):
    portfolio_detail = get_object_or_404(Portfolio,pk=pk)
    generalsetting = Generalsetting.objects.get(id=1)
    context = {
        'portfolio_detail':portfolio_detail,
         'generalsetting' : generalsetting, 
        
    }
    
    return render(request,'companyapp/portfolio_detail.html',context)



def contact_f(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contactform.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            date_message = timezone.now()
            
        )
    
    
    return redirect('home')
    