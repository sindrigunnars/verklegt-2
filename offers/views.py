from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, time
from cart.models import Order, OrderOffer
from menu.models import Pizza
from .models import Offer, NewOrder, OrderItem


# Create your views here.


def index(request):
    curr_time = datetime.utcnow().time()
    active_time = False
    if time(11, 00) <= curr_time <= time(13, 00):
        active_time = True
    context = {
        'offers': Offer.objects.all().order_by('name'),
        'active': active_time
    }
    return render(request, 'offers/index.html', context)


def get_offer_by_id(request, id):
    offer = get_object_or_404(Offer, pk=id)
    if offer.id == 1:
        return render(request, 'offers/two_for_one.html', {
            'offer': offer,
            'pizzas': Pizza.objects.all()
        })
    elif offer.id == 3:
        return render(request, 'offers/internet_offer.html', {
            'offer': offer,
            'pizzas': Pizza.objects.all()
        })
    elif offer.id == 2:
        return render(request, 'offers/lunch_offer.html', {
            'offer': offer,
            'pizzas': Pizza.objects.all()
        })
    else:
        return render(request, 'offers/index.html', {
            'offer': offer,
            'pizzas': Pizza.objects.all()
        })

def get_pizza_by_id(request, id):
    return render(request, 'offers/two_for_one.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def add_offer_to_cart(request):
    pizza1 = request.POST.get('pizza1', None)
    pizza2 = request.POST.get('pizza2', None)
    offer_id = request.POST.get('OfferID', None)

    if pizza1 and offer_id:
        pizza_object1 = Pizza.objects.get(pk=pizza1)
        new_offer = NewOrder.objects.create(order=Offer.objects.get(pk=offer_id))
        new_offer.items.add(OrderItem.objects.create(item=pizza_object1))

        if pizza2:
            pizza_object2 = Pizza.objects.get(pk=pizza2)
            new_offer.items.add(OrderItem.objects.create(item=pizza_object2))
            new_offer.price = max(pizza_object1.price, pizza_object2.price)
        else:
            new_offer.price = 2000
        new_offer.save()

        try:
            cart_order = Order.objects.get(order_user=request.user, completed=False)
            cart_order.offers.add(OrderOffer.objects.create(item=new_offer))
            cart_order.price += new_offer.price
            cart_order.save()
        except Order.DoesNotExist:
            new_order = Order.objects.create(order_user=request.user)
            new_order.offers.add(OrderOffer.objects.create(item=new_offer))
            new_order.price += new_offer.price
            new_order.save()
        except TypeError:
            return redirect('login')

    return redirect('offers-index')