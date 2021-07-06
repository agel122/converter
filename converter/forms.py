from django import forms


class Adder(forms.Form):
    added_data = forms.CharField(label='weight in grams', error_messages={'required': 'input your data'}, max_length=50)
