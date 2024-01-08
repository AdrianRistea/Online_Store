from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator
from django.forms import TextInput

from store.models import Product, Category


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email address'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please re-enter your password'})


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class SpecialPriceForm(forms.Form):
    special_price = forms.DecimalField(label='Special Price', max_digits=8, decimal_places=2)


class CategoryForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter product name', 'class': 'form-control'}),
            'discount_price_valid_until': TextInput(
                attrs={'placeholder': 'Year  Month  Day ', 'class': 'form-control'}),
        }

        def clean(self):
            cleaned_data = self.cleaned_data
            check_emails = Product.objects.filter(email=cleaned_data['email'])
            if check_emails:
                msg = 'Aceasta adresa de mail exista deja in db'
                self._errors['email'] = self.error_class([msg])

            if 'image' in cleaned_data and not cleaned_data['image']:
                self.add_error('image', 'Please upload an image for the product.')

            get_start_date = cleaned_data['start_date']
            get_end_date = cleaned_data['end_date']
            if get_start_date > get_end_date:
                msg = 'Start date-ul introdus este mai mare decat end date'
                self._errors['start_date'] = self.error_class([msg])

            return cleaned_data


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(label='Adresa de livrare', widget=forms.Textarea(attrs={'rows': 3}))
    billing_address = forms.CharField(label='Adresa de facturare', widget=forms.Textarea(attrs={'rows': 3}))
    # card_number = forms.CharField(label='Numar card', max_length=16)
    # card_expiry = forms.CharField(label='Data expirate card', max_length=5, help_text='MM/YY')
    # card_cvc = forms.CharField(label='Card CVC', max_length=3)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'active', 'parent_category']
