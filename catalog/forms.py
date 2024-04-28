from django import forms

from catalog.models import Products, Version


class StyleFormMixin:
    """
    Класс примесь стилей форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = ''


class ProductsForm(StyleFormMixin,
                   forms.ModelForm):
    """
    Форма класса продукта
    """

    class Meta:
        model = Products
        exclude = ('created_at', 'updated_at', 'seller')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенное имя')

            return cleaned_data


class ModeratorFormProducts(StyleFormMixin,
                            forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_description', 'product_category', 'publication_sign')


class VersionForm(StyleFormMixin, forms.ModelForm):
    """
    Форма класса версий продукта
    """

    class Meta:
        model = Version
        fields = '__all__'
