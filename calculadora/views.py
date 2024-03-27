from django.shortcuts import render

# Vista para mostrar el formulario
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'calculadora/formulario.html', context)

def calcular(request):
    if request.method == 'POST':
        numero1 = float(request.POST['numero1'])
        numero2 = float(request.POST['numero2'])
        operacion = request.POST['operacion']
        resultado = None

        if operacion == 'suma':
            resultado = numero1 + numero2
        elif operacion == 'resta':
            resultado = numero1 - numero2
        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2

        context = {
            'titulo': "Resultado",
            'numero1': numero1,
            'numero2': numero2,
            'operacion': operacion.capitalize(),
            'resultado': resultado,
        }
        return render(request, 'calculadora/respuesta.html', context)
    else:
        return render(request, 'calculadora/formulario.html', {'titulo': "Calculadora"})
