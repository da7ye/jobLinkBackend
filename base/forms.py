
from django import forms
from base.models import Provider


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            'profile_photo',
            'name',
            'last_name',
            'email',
            'gender',
            'phone_number',
            'price',
            'categories',
            'description_small',
            'description_big',
        ]