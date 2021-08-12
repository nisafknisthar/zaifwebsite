from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse,HttpResponseRedirect
from apps.models import *
import json
# Create your views here.



def index(request):
    pic = Picture.objects.filter(featured=True).select_related()[:6]
    slider = Slider.objects.all()
    variables = RequestContext(request,{'pic':pic,'slider':slider})
    return render_to_response('index.html', variables)

def about(request):
    testimonial = Testimonial.objects.filter(is_approved=True).select_related()
    variables = RequestContext(request,{'testimonial':testimonial})
    return render_to_response('about-us.html', variables)

def contact(request):

    print "contact page loading ..."

    if request.POST:

        response_data={}

        print "contact "

        try:

            name=request.POST.get('name')
            message=request.POST.get('message')
            email=request.POST.get('email')
            phone=request.POST.get('phone')

            if name and message and phone and email :

                data=Contact(name=name,phone=phone,message=message,email=email)

                data.save()

                response_data['status'] = "success"
            else:
                response_data['status'] = "nullval"
                return HttpResponse(json.dumps(response_data), content_type='application/json')
        except Exception, e:
            print e

            response_data['status'] = "fail"
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    variables = RequestContext(request)
    return render_to_response('contact-us.html', variables)

def products(request):
    catagories = Category.objects.all()
    pic =Picture.objects.all()[:12]
    variables = RequestContext(request,{'catagories':catagories, 'pic':pic})
    return render_to_response('products.html', variables)

def product_filter(request, slug):
    catagories = Category.objects.all()
    print catagories
    print"inside product"
    # cat=request.GET.get('slug')
    # print cat
    print slug
    if slug:
        pic =Picture.objects.filter(category__slug=slug)
        print "inside cat"

    else:
        pic =Picture.objects.all()[:6]

    variables = RequestContext(request,{'pic':pic,'catagories':catagories})
    return render_to_response('products.html', variables)

def details(request):
    variables = RequestContext(request)
    return render_to_response('single-post.html', variables)

def testimonial(request):


    print "Testimonial page loading ..."

    if request.POST:

        response_data={}

        print "testimonial "

        try:

            name=request.POST.get('tname')
            message=request.POST.get('tmessage')
            email=request.POST.get('temail')
            phone=request.POST.get('tphone')



            if name and message and phone and email :

                data=Testimonial(name=name,phone=phone,message=message,email=email)

                data.save()

                response_data['status'] = "success"
            else:

                response_data['status'] = "nullval"
                return HttpResponse(json.dumps(response_data), content_type='application/json')
        except Exception, e:
            print e

            response_data['status'] = "fail"
        return HttpResponse(json.dumps(response_data), content_type='application/json')



    else:

        variables=RequestContext(request,{})
        return render_to_response('about.html',variables)
