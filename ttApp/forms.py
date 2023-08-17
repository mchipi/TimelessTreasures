from django import forms
from . import models

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)


    class Meta:
        model = models.Product
        exclude = ['seller', 'id', 'bought']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD;'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD; height: 100px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD; height: 100px;'}),
            'specs': forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD; height: 100px;'}),
            'shipping_info': forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD; height: 100px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD'}),
            'img': forms.FileInput(attrs={'class': 'form-control', 'style': 'background-color: #2F3234; border-color: #878889; color: #ADB5BD'}),
        }