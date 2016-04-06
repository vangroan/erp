
from django.conf.urls import url

from erp.distribution.views import StockItemListView

urlpatterns = (
    url(r'stockitem/$', StockItemListView.as_view(), name='stockitem-list'),
)
