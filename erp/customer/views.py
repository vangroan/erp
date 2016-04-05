
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from erp.customer.models import Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerListView(ListView):
    model = Customer
