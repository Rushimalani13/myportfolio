from django.http import HttpResponse
from django.template import loader
from homep.models import Contactdb
from django.views.decorators.csrf import csrf_exempt


def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@csrf_exempt
def contact(request):
  if request.method=="POST":
    email=request.POST['email']
    name=request.POST['name']
    concern=request.POST['concern']
    city =request.POST['city']
    state =request.POST['state']
    zip =request.POST['zip']
    contact=Contactdb(email=email,name=name,concern=concern,city=city,state=state,zip=zip)
    contact.save()
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def adminpanel(request):
  mydata = Contactdb.objects.all()
  template = loader.get_template('adminpanel.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))