
from django.forms import ModelForm

from erp.customer.models import Customer


class CustomerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['account_number'].widget.attrs['readonly'] = True

    def clean_account_number(self):
        if self.instance and self.instance.pk:
            return self.instance.account_number
        else:
            return self.cleaned_data['account_number']

    class Meta:
        fields = ['account_number', 'name']
        model = Customer
