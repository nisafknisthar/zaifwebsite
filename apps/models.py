from django.db import models
from imagekit.models import ProcessedImageField
from django.conf.urls import patterns, url, include
#slugify
from apps.slug import unique_slugify

from unidecode import unidecode
from django.core.urlresolvers import reverse
from solo.models import SingletonModel



class Category(models.Model):
    name = models.CharField(verbose_name='Name',null=True,blank=True,max_length = 20)
    slug = models.SlugField(max_length=1000,unique=True,null=True,blank=True)


    def save(self):
        if not self.slug:
            name = unidecode(self.name)
            unique_slugify(self,name)

        super(Category,self).save()
    def __unicode__(self):
        return self.name

class Picture(models.Model):

    heading = models.CharField(verbose_name='Main Heading',null=True,blank=True,max_length = 70)
    content = models.CharField(verbose_name='Content',null=True,blank=True,max_length = 70)
    category = models.ForeignKey(Category)
    image = ProcessedImageField(upload_to='images/picture',options={'quality': 60},verbose_name = "Product Image")
    single = ProcessedImageField(upload_to='images/single pic',options={'quality': 60},verbose_name = "Single Tile Image")
    featured=models.BooleanField(default=False,verbose_name="Featured Product or Not")
    slug = models.SlugField(max_length=1000,unique=True,null=True,blank=True)


    def save(self):
        if not self.slug:
            heading = unidecode(self.heading)
            unique_slugify(self,heading)

        super(Picture,self).save()


    def __unicode__(self):
        return self.heading

    class Meta:
        verbose_name = ("Picture")
        verbose_name_plural = ("Pictures")
class SiteConfiguration(SingletonModel):

    site_name = models.CharField(max_length=255, default='Site Name')

    email=models.EmailField(max_length=70,blank=True, null= True, unique= True)

    fb_url = models.URLField(verbose_name = "Facebook",blank = True, default='')

    twitter_url = models.URLField(verbose_name = "Twitter",blank = True, default='')

    linkedin_url = models.URLField(verbose_name = "Linkedin",blank = True, default='')

    logo = models.ImageField(upload_to = "images/logo",verbose_name = "logo 125*100 px",default='')

    maintenance_mode = models.BooleanField(default=False)

    def __unicode__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

class Contact(models.Model):

    name = models.CharField(max_length = 250,blank=True, null= True,verbose_name = "Name")

    email = models.EmailField(max_length=70,blank=True, null= True,verbose_name = "Email ID")
    message = models.TextField(max_length=70, verbose_name = "Message", blank=True, null= True)
    phone = models.CharField(max_length = 250,blank=True, null= True,verbose_name = "Phone_number")
    def __unicode__(self):
        return self.name



    class Meta:
        verbose_name = ("Contactus ")
        verbose_name_plural = ("Contactus ")

class Testimonial(models.Model):
    email=models.CharField(max_length = 250,verbose_name = "Email",default='')
    message = models.TextField(verbose_name = "Message")
    name = models.CharField(max_length = 250,verbose_name = "Name")
    is_approved=models.BooleanField(default=False,verbose_name="Testimonial approved or Not")
    phone  = models.CharField(max_length = 500,blank=True, null= True,verbose_name = "Number")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

class Slider(models.Model):

    heading = models.CharField(verbose_name='Main Heading',null=True,blank=True,max_length = 70)
    content = models.CharField(verbose_name='Content',null=True,blank=True,max_length = 70)
    image = ProcessedImageField(upload_to='images/slider',
                                options={'quality': 60},verbose_name = "Slider Image")


    def __unicode__(self):
        return self.heading

    class Meta:
        verbose_name = ("Slider")
        verbose_name_plural = ("Sliders")
