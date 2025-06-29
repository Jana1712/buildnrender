from django.contrib import admin

from .models import FAQ, About, Contactform, Generalsetting, Portfolio, Service, Slider, Team 

# Register your models here.
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Team)
admin.site.register(FAQ)
admin.site.register(Contactform)
admin.site.register(Generalsetting)

