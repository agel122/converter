from django.shortcuts import render
from .forms import Adder
from .converter_type import *


def home(request):
    return render(request, 'base.html')


def converter(request):
    if request.method == 'POST':
        form = Adder(request.POST)
        if form.is_valid():
            try:
                converter_name=form.cleaned_data['selected_converter']
                value_to_convert = int(form.cleaned_data['added_data'])
                return render(request, 'converter.html',
                              {'result': dispatcher[converter_name](value_to_convert)['result'],
                               'initial_value': value_to_convert,
                               'initial_unit': dispatcher[converter_name](value_to_convert)['initial_unit'],
                               'result_unit': dispatcher[converter_name](value_to_convert)['result_unit']})
            except ValueError as e:
                e.message = 'Enter the number, not the string'
                return render(request, 'converter.html', {'message': e.message})
    else:
        form = Adder()
    return render(request, 'converter.html', {'form': form})


