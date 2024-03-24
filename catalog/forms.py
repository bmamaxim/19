from django import forms

from catalog.models import Products


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        exclude = ('created_at', 'updated_at',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенное имя')

            return cleaned_data
