from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from flowerApp.models import Flower


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    cart_id = _cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id)
        cart.save()
    try:
        cart_item = CartItem.objects.get(flower=flower, cart=cart)
        if cart_item.quantity < cart_item.flower.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            flower=flower,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('Cart:cart_detail')


def cart_detail(request):
    cart_id = _cart_id(request)
    cart = get_object_or_404(Cart, cart_id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    total = 0
    counter = 0
    for item in cart_items:
        total += item.flower.price * item.quantity
        counter += item.quantity
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
    }
    return render(request, 'cart_detail.html', context)


def remove_from_cart(request, flower_id):
    cart_id = _cart_id(request)
    cart = get_object_or_404(Cart, cart_id=cart_id)
    flower = get_object_or_404(Flower, id=flower_id)
    cart_item = CartItem.objects.get(cart=cart, flower=flower)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart:cart_detail')


def delete_cart(request, flower_id):
    cart_id = _cart_id(request)
    cart = get_object_or_404(Cart, cart_id=cart_id)
    flower = get_object_or_404(Flower, id=flower_id)
    cart_item = CartItem.objects.get(cart=cart, flower=flower)
    cart_item.delete()
    return redirect('Cart:cart_detail')


def checkout(request):
    return render(request, 'checkout.html')
