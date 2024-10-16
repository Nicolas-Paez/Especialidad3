from django.shortcuts import get_object_or_404, redirect, render
from .models import Formulario, Pregunta, Opcion
from django.core.mail import send_mail

def crear_formulario(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        preguntas = request.POST.getlist('preguntas')

        formulario = Formulario.objects.create(titulo=titulo)
        
        for index, pregunta_texto in enumerate(preguntas, start=1):
            pregunta = Pregunta.objects.create(formulario=formulario, texto=pregunta_texto)
            opciones = request.POST.getlist(f'opciones_{index}[]')
            correcta = int(request.POST[f'correcta_{index}'])

            for i, opcion_texto in enumerate(opciones):
                Opcion.objects.create(pregunta=pregunta, texto=opcion_texto, es_correcta=(i == correcta))

        return redirect('ver_formulario', formulario_id=formulario.id)  # Cambia 'id' por 'formulario_id'

    return render(request, 'crear_formulario.html')

def ver_formulario(request, formulario_id):  # Cambia 'id' por 'formulario_id'
    formulario = get_object_or_404(Formulario, id=formulario_id)
    return render(request, 'ver_formulario.html', {'formulario': formulario})

def eliminar_formulario(request, id):
    formulario = get_object_or_404(Formulario, id=id)
    formulario.delete()  # Esto eliminará el formulario
    return redirect('home')  # Redirige a la lista de formularios después de eliminar

def responder_formulario(request, formulario_id):
    formulario = get_object_or_404(Formulario, id=formulario_id)
    preguntas = formulario.preguntas.all()

    if request.method == 'POST':
        estudiante_id = request.POST['estudiante_id']
        respuestas = []
        correctas = 0

        for pregunta in preguntas:
            opcion_seleccionada = int(request.POST[f'pregunta_{pregunta.id}'])
            opcion_correcta = Opcion.objects.get(pregunta=pregunta, es_correcta=True)

            respuestas.append({
                'pregunta_id': pregunta.id,
                'opcion_seleccionada': opcion_seleccionada
            })

            if opcion_seleccionada == opcion_correcta.id:
                correctas += 1

        # Calcular la nota
        nota = (correctas / len(preguntas)) * 10 if preguntas else 0

        # Guardar en MongoDB (Modelo Resultado)
        from .models import Resultado
        resultado = Resultado.objects.create(estudiante_id=estudiante_id, respuestas=respuestas, nota=nota)

        # Enviar correo con el resultado
        send_mail(
            'Resultado de la prueba',
            f'Has obtenido una nota de: {nota}',
            'noreply@tuapp.com',
            [request.POST['email']]
        )

        return render(request, 'resultado.html', {'nota': nota})

    return render(request, 'responder_formulario.html', {'formulario': formulario, 'preguntas': preguntas})



def home(request):
    formularios = Formulario.objects.all()
    return render(request, 'home.html', {'formularios': formularios})
