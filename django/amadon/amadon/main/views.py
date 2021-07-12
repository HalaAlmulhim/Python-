from django.shortcuts import render, redirect
from .models import Order, Product

# Create your views here.
def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout(request):
    quant = 0
    total_order = 0
    for item in Order.objects.all():
        quant += item.quantity_ordered
        total_order += item.total_price

    context = {
        "total_quantity" : quant,
        "total_order" : total_order,
    }
    return render(request, "store/checkout.html", context)


def process(request):
    quantity_from_form = int(request.POST["quantity"])
    product_from_form = request.POST["product"]
    price = float(Product.objects.get(description=product_from_form).price)
    total_charge = quantity_from_form * price
    request.session['total_charge'] = total_charge
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout")