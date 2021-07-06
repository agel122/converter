from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def weigth_converter(request):
    if request.method == 'POST':
        value_in_g = int(request.POST['value_in_g'])
        result_kg = value_in_g/1000
        return render(request, 'weight_converter.html', {'result': result_kg, 'initial_value': value_in_g,})
    return render(request, 'weight_converter.html')
