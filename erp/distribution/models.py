
from datetime import datetime

from django.db.models import Model
from django.db.models import CharField
from django.db.models import AutoField, DateTimeField
from django.db.models import ForeignKey

from erp.customer.models import Customer


class StockItem(Model):

    ACTIVE = 'A'
    ONHOLD = 'H'
    DISCONTINUED = 'D'

    ItemStatus = (
        (ACTIVE, 'Active'),
        (ONHOLD, 'OnHold'),
        (DISCONTINUED, 'Discontinued'),
    )

    code = CharField(max_length=20, unique=True)
    description = CharField(max_length=100, default='')
    status = CharField(max_length=1, choices=ItemStatus)

    # TODO: Price lists and Prices


class DistributionDocument(Model):

    ENTERED = 'E'
    UNPROCESSED = 'U'
    PROCESSED = 'P'
    CANCELLED = 'C'

    DocumentStatus = (
        (ENTERED, 'Entered'),
        (UNPROCESSED, 'Unprocessed'),
        (PROCESSED, 'Processed'),
        (CANCELLED, 'Cancelled'),
    )

    prefix = CharField(max_length=20)
    reference = CharField(max_length=50)
    status = CharField(max_length=1, choices=DocumentStatus, default=ENTERED)
    created = DateTimeField()
    updated = DateTimeField()

    @staticmethod
    def generate_reference(document):
        return '{prefix}{number:06d}'.format(prefix=document.prefix, number=document.id)

    def save(self):
        if not self.pk:
            self.reference = self.generate_reference(self)
            self.created = datetime.utcnow()
        updated = datetime.utcnow()
        super(DistributionDocument, self).save()

    class Meta:
        abstract = True


class SalesOrder(DistributionDocument):

    customer = ForeignKey(Customer)
    customer_account_number = CharField(max_length=20)

    def save(self):
        if not self.pk:
            customer_account_number = self.customer.account_number
        super(SalesOrder, self).save()


class SalesOrderLine(Model):

    stockitem = ForeignKey(StockItem)
    sales_order = ForeignKey(SalesOrder)
