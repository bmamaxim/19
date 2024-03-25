from django import forms

from catalog.models import Products, Version


class ProductsForm(forms.ModelForm):
    """
    Форма класса продукта
    """

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


class VersionForm(forms.ModelForm):
    """
    Форма класса версий продукта
    """

    class Meta:
        model = Version
        fields = '__all__'

