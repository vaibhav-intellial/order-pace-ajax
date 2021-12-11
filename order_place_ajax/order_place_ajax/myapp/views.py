from django.db.models.base import Model
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import json
from .models import Order, OrderItem, Product

# Create your views here.


def form(request):
    allproduct = Product.objects.all()
    allorderitem = OrderItem.objects.all()
    return render(request, "form.html", {"allorderitem": allorderitem, "allproduct": allproduct})


def addorder(request):

    firstname = request.GET["firstname"]
    lastname = request.GET["lastname"]
    email = request.GET["email"]
    address_street = request.GET["address_street"]
    address_landmark = request.GET["address_landmark"]
    address_pincode = request.GET["address_pincode"]
    product = request.GET["product"]
    quantity = request.GET["quantity"]
    prize = request.GET["prize"]

    orderobj = Order.objects.create(
        firstname=firstname, lastname=lastname, email=email, address_landmark=address_landmark, address_street=address_street, address_pincode=address_pincode
    )
    orderitemobj = OrderItem.objects.create(product_id=product, order_id=orderobj.id, quantity=quantity, prize=prize)

    return HttpResponse("true")


def vieworder(request):
    allorderitem = OrderItem.objects.all()
    return JsonResponse(json.dump(allorderitem))
