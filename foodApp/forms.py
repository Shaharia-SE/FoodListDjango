from django.forms import forms
from .models import Item


class ItemForm(forms.Form):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
