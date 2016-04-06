
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from erp.customer.models import Customer
from erp.customer.forms import CustomerForm


class CustomerDetailView(DetailView):
    model = Customer


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm

    def get_success_url(self):
        return reverse('customer-detail', kwargs={'pk':self.object.pk})


class CustomerEditView(UpdateView):
    model = Customer
    form_class = CustomerForm
