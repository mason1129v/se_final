from django.shortcuts import render
from .models import *
# Create your views here.

def index_view(request):
    record = RevenueRecord.objects.all()
    revenue_amount_list = [entry.revenue_amount for entry in record]
    print(revenue_amount_list)
    return render(request, 'index.html', locals())


def client_view(request):
    return render(request, 'client.html', locals())


def product_mc_view(request):
    return render(request, 'product_mc.html', locals())


def public_mc_view(request):
    return render(request, 'public_mc.html', locals())


def sales_view(request):
    return render(request, 'sales.html', locals())


def store_view(request):
    return render(request, 'store.html', locals())
