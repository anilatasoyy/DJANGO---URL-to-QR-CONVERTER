from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(label = "Enter URL of QR code:")