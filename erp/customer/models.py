
from datetime import datetime

from django.db.models import Model
from django.db.models import CharField, DateTimeField


class Customer(Model):

    CustomerType = (
        # Commercial
        ('HD', 'Head Branch'),
        ('BR', 'Branch'),
        ('ID', 'Individual'),

        # Academic
        ('IN', 'Institution'),
        ('CN', 'Centre'),
        ('PT', 'Parent'),
        ('ST', 'Student'),
    )

    account_number = CharField(max_length=20)
    name = CharField(max_length=255)
    first_name = CharField(max_length=255, null=True)
    last_name = CharField(max_length=255, null=True)

    updated = DateTimeField()
    created = DateTimeField()

    # TODO: Main-Sub account link, where main is responsible for account
    # TODO: Main-Sub account link, where sub is responsible for account

    def save(self):
        if not self.id:
            if not self.account_number:
                self.account_number = generate_account_number(self)
            self.created = datetime.now()
        self.updated = datetime.now()
        super(Customer, self).save()

    @staticmethod
    def generate_account_number(customer):
        return '%s' % (name[:4].upper(),)


class Address(Model):

    AddressTypes = (
        ('D', 'Delivery Address'),
        ('B', 'Billing Address')
    )

    address_type = CharField(max_length=1, choices=AddressTypes)
    street = CharField(max_length=40)
    postcode = CharField(max_length=10)

    # TODO: Associate with carrier
    # TODO: Provinces
