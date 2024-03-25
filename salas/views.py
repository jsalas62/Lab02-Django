from django.shortcuts import render

# Vista para mostrar el formulario
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'salas/formulario.html', context)

# Vista para procesar el formulario y mostrar la respuesta
def formulario(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render (request, 'salas/respuesta.html', context)
