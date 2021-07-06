from django.shortcuts import render
from .forms import Adder


def home(request):
    return render(request, 'base.html')


def weigth_converter(request):
    if request.method == 'POST':
        form = Adder(request.POST)
        if form.is_valid():
            try:
                value_in_g = int(form.cleaned_data['added_data'])
                result_kg = value_in_g/1000
                return render(request, 'weight_converter.html',
                              {'result': result_kg, 'initial_value': value_in_g,})
            except ValueError as e:
                e.message = 'Enter the number, not the string'
                return render(request, 'weight_converter.html', {'message': e.message})
    else:
        form = Adder()
    return render(request, 'weight_converter.html', {'form': form})

