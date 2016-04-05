
from django.db.models import Model
from django.db.models import CharField


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

    name = CharField(max_length=255)
    first_name = CharField(max_length=255, null=True)
    last_name = CharField(max_length=255, null=True)

    # TODO: Main-Sub account link, where main is responsible for account
    # TODO: Main-Sub account link, where sub is responsible for account


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
