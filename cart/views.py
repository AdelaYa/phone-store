from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Phone
from .cart import Cart
from .forms import CartAddPhoneForm


@require_POST
def cart_add(request, slug):
    cart = Cart(request)
    phone = get_object_or_404(Phone, slug=slug)
    form = CartAddPhoneForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(phone=phone,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, slug):
    cart = Cart(request)
    phone = get_object_or_404(Phone, slug=slug)
    cart.remove(phone)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

