from django import forms

GROUP_NAME_SET = [
        ('weight_converter', 'convert g -> kg'),
    ]


class Adder(forms.Form):
    selected_converter = forms.ChoiceField(label='Selected Converter', choices=GROUP_NAME_SET)
    added_data = forms.CharField(label='Value to convert',
                                 error_messages={'required': 'input your data'},
                                 max_length=50)
