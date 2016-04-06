
from django.conf.urls import url

from erp.customer.views import CustomerDetailView, CustomerListView
from erp.customer.views import CustomerCreateView, CustomerEditView

urlpatterns = (
    url(r'create/$', CustomerCreateView.as_view(), name='customer-create'),
    url(r'(?P<pk>\d)/edit/$', CustomerEditView.as_view(), name='customer-edit'),
    url(r'(?P<pk>\d)/$', CustomerDetailView.as_view(), name='customer-detail'),
    url(r'$', CustomerListView.as_view(), name='customer-list'),
)
