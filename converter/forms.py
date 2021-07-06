from django import forms


class Adder(forms.Form):
    added_data = forms.CharField(label='Added_Data', max_length=50)
