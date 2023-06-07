from django.shortcuts import render
from .models import *
# Create your views here.

def index_view(request):
    record = RevenueRecord.objects.all()
    revenue_amount_list = [entry.revenue_amount for entry in record]
    print(revenue_amount_list)
    return render(request, 'index.html', locals())