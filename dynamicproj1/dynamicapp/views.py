from django.shortcuts import render
from . models import Place
from . models import Person
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Person.objects.all()
    return render(request,"index.html",{'obj1':obj,'objj':obj2})
