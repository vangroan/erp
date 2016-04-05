
from django.conf.urls import url

from erp.customer.views import CustomerDetailView, CustomerListView

urlpatterns = (
    url(r'/(?P<id>\d)/$', CustomerDetailView.as_view(), name='customer-detail'),
    url(r'$', CustomerListView.as_view(), name='customer-list'),
)
