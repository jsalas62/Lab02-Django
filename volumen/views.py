from django.shortcuts import render
from math import pi

def index(request):
    context = {
        'titulo': "Calculadora de Volumen de Cilindro",
    }
    return render(request, 'volumen/formulario.html', context)

def calcular_volumen(request):
    if request.method == 'POST':
        altura = float(request.POST.get('altura'))
        diametro = float(request.POST.get('diametro'))
        radio = diametro / 2
        volumen = pi * radio**2 * altura
        context = {
            'titulo': "Resultado",
            'altura': altura,
            'diametro': diametro,
            'volumen': volumen,
        }
        return render(request, 'volumen/respuesta.html', context)
    else:
        return render(request, 'volumen/formulario.html', {'titulo': "Calculadora de Volumen de Cilindro"})
