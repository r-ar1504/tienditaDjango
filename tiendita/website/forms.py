from django import forms

class ContactoForm(forms.Form):
	nombre = forms.CharField(required=True)
	asunto = forms.CharField(required=True)
	email = forms.CharField(required=True)
	mensaje = forms.CharField(required=True, widget=forms.Textarea)