from math import ceil
from multiprocessing import context
from django.shortcuts import render

from tracker.scraper.scrapper_amazon import scrapper_amazon
from .scraper import scrapper_amazon,scrapper_elitehub,scrapper_flipkart

from tracker.models import Product

# Create your views here.
def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()
    n=len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    context = {'product':products,'no_of_slides': nSlides,'range': range(nSlides)}
    return render(request,'home.html', context)

def about(request):
    context = {}
    return render(request,'about.html', context)

def product(request,myid):
    #fetch product using id
    product = Product.objects.filter(id = myid)
    elitehub = scrapper_elitehub.scrapper_elitehub.__price__(product[0].elitehub)
    amazon = scrapper_amazon.scrapper_amazon.__price__(product[0].amazon)
    flipkart = scrapper_flipkart.scrapper_flipkart.__price__(product[0].flipkart)
    context = {'product': product[0],'elitehub':elitehub,'amazon': amazon, 'flipkart': flipkart}
    return render(request,'product.html', context)

def search(request):
    return
