from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from ttApp import forms
from ttApp.forms import ProductForm
from ttApp.models import Product, Favorite


def index(request):
    context = {"form": ProductForm}
    return render(request, 'index.html', context=context)


def add_product(request):
    if request.method == "POST":
        form = forms.ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            context = {"product": product}
            return render(request, 'product_action.html', context=context)
    context = {"form": ProductForm}
    return render(request, 'add_product.html', context=context)


def list(request):
    products = Product.objects.exclude(Q(seller=request.user) | Q(bought=True))
    context = {"form": ProductForm, "products": products}
    return render(request, 'list.html', context=context)


def details(request, id):
    product = Product.objects.get(id=id)
    try:
        favorite = Favorite.objects.get(user=request.user, product=product)
    except Favorite.DoesNotExist:
        favorite = None
    context = {"product": product, "favorite": favorite}
    return render(request, 'details.html', context=context)


def my_store(request):
    products = Product.objects.filter(seller=request.user, bought=False)
    context = {"products": products}
    return render(request, 'list.html', context=context)


def add_to_favorites(request, id):
    product = Product.objects.get(id=id)
    favorite = Favorite(user=request.user, product=product)
    favorite.save()
    return redirect('details', id=id)


def remove_from_favorites(request, id):
    product = Product.objects.get(id=id)
    favorite = Favorite.objects.get(user=request.user, product=product)
    favorite.delete()
    return redirect('details', id=id)


def favorites(request):
    favorites = Favorite.objects.filter(user=request.user, product__bought=False)
    favorite_products = [fave.product for fave in favorites]
    context = {"products": favorite_products}
    return render(request, 'list.html', context=context)


def product_action(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, 'product_action.html', context=context)


def buy(request, id):
    product = Product.objects.get(id=id)
    product.bought = True
    product.save()
    context = {"product": product}
    return render(request, 'product_action.html', context=context)

# Create your views here.
