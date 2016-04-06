
from django.shortcuts import render
from django.views.generic import ListView

from erp.distribution.models import StockItem


class StockItemListView(ListView):
    model = StockItem
