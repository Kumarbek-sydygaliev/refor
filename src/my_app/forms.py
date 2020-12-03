from django import forms

class LinksForm(forms.Form):
    link = forms.URLField()
    link.widget.attrs.update:({
        'class': 'Form-control',
        'placeholder': 'Enter your link'})
    