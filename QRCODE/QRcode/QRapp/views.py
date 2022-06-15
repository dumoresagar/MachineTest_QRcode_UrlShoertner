from django.shortcuts import render,redirect
from .models import Url,Website

# Create your views here.


def createUrl(request):
    if request.method == 'POST':
        full_url = request.POST.get('full_url')
        obj = Url.create(full_url)
        template_name = 'home.html'
        context = {'full_url': obj.full_url, 'short_url': request.get_host() + '/' + obj.short_url}
        return render(request, template_name, context)
    template_name = 'home.html'
    return render(request, template_name)

def newurl(request,key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(createUrl)



def home_view(request):
  name = 'Welcome to'
  obj = Website.objects.get(id=1)
  context = {
    'name': name,
    'obj': obj,
  }
  return render(request, 'qrcode.html', context)

