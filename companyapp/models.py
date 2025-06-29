from django.db import models

# Create your models here.
# Slider
class Slider(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(max_length=500,default='')
    image = models.ImageField(upload_to='image_slider')
    
    
    def __str__(self):
        return self.title
    
    
    # About
class About(models.Model):
    title = models.CharField(max_length=200,db_default='')
    image1 = models.ImageField(upload_to='image1_about',null=True,blank=True)
    description = models.TextField(max_length=600,default='')
    short_description1 = models.TextField(max_length=600,db_default='')
    title_headline1 = models.CharField(max_length=100,db_default='')
    title_headline2 = models.CharField(max_length=100,db_default='')
    title_headline3 = models.CharField(max_length=100,db_default='')
    short_description2 = models.TextField(max_length=600,db_default='')
    image2 = models.ImageField(upload_to='image2_about',null=True,blank=True)
    video = models.CharField(max_length=100,db_default='')
    
    
    def __str__(self):
        return self.title    
    
    
    # Services
    
class Service(models.Model):
    icon_service = models.CharField(max_length=100,db_default='')
    title = models.CharField(max_length=100,default='')
    description = models.TextField(max_length=300,default='')
    speed = models.TextField(max_length=100,default='')
    
    
    def __str__(self):
        return self.title 
    
    
    #Portfolio

class Portfolio(models.Model):
    category = models.CharField(max_length=100,db_default='')
    title = models.CharField(max_length=200,db_default='')
    short_description = models.TextField(max_length=500,default='')
    clients = models.CharField(max_length=100,default='')
    url = models.CharField(max_length=100,default='')
    description = models.TextField(max_length=1000,db_default='')
    image = models.ImageField(upload_to='image_portfolio')
    
    
    
    def __str__(self):
        return self.title
         
         
         
    #Team
    
       
class Team(models.Model):
    fullname = models.CharField(max_length=100,db_default='')
    role_company = models.CharField(max_length=100,db_default='')
    image = models.ImageField(upload_to='image_team')
    url_x = models.CharField(max_length=100,default='')
    url_facebook = models.CharField(max_length=100,default='')
    url_instagram = models.CharField(max_length=100,default='')
    url_linkedin = models.TextField(max_length=100,default='')
    speed = models.TextField(max_length=100,default='')
    
    
    
    def __str__(self):
        return self.fullname
    
             
             
    # FAQ
    
    
class FAQ(models.Model):
    question = models.CharField(max_length=200,db_default='')
    reply = models.TextField(max_length=1000,default='')
    speed = models.CharField(max_length=100,db_default='')
    
    
    
    def __str__(self):
        return self.question      
    
    
    
    #contact
    
class Contactform(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.EmailField()
    subject = models.CharField(max_length=200,default='')
    message = models.TextField()
    date_message = models.DateField(null = True, blank=True)
    
    def __str__(self):
        return self.email
        
        
        
    #General Setting
    
class Generalsetting(models.Model):
    favicon = models.ImageField(upload_to='image_favicon', null=True, blank=True)
    logo = models.ImageField(upload_to='image_logo', null=True, blank=True)
    companyname = models.CharField(max_length=100,default='')
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=200,default='')
    url_x = models.CharField(max_length=100,default='')
    url_facebook = models.CharField(max_length=100,default='')
    url_instagram = models.CharField(max_length=100,default='')
    url_linkedin = models.CharField(max_length=100,default='')
    
    
    
    def __str__(self):
        return self.companyname
    
    
            