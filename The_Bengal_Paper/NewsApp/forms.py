from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Enter title (e.g. company name)'})
    )
    link = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder':'Enter the link to where to redirect'}),
        required=False
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Tell us about the advertisement (Optional)'}),
        label='Description (optional)',
        required=False
    )
    validity = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date'}),
        
        label='Validity (Days)',
        required=False
    )
    class Meta:
        model = Advertisement
        fields = ['title', 'image', 'link', 'content', 'validity']