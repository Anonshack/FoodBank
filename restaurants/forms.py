from django import forms
from .models import Restaurant
from .snippets import choices


class RestaurantCreateForm(forms.ModelForm):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter title'}))
    categories = forms.CharField(label="Categories", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categories separated by comma. Example: chinese,thai'}))
    image = forms.ImageField(label="Image", widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(label="Location", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}))
    price = forms.IntegerField(label="Price", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}))
    vat = forms.IntegerField(label="VAT", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'VAT in %'}))
    taste = forms.ChoiceField(label="Taste", widget=forms.Select(attrs={'class': 'form-control'}), choices=choices)
    persons = forms.ChoiceField(label="Persons", widget=forms.Select(attrs={'class': 'form-control'}), choices=choices)
    details = forms.CharField(label="Details", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Restaurant
        fields = ['title', 'image', 'categories', 'location', 'price', 'vat', 'taste', 'persons', 'details']
