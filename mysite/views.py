import contextlib
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
def saludar(request):
    saludo="Hola Django - Coder"
    pagina_html=HttpResponse(saludo)
    return pagina_html

def segunda_vista(request):
    return HttpResponse ("<br><br>Ya entendimos esto, es muy simple :)")

def saludar_con_html(request):
    http_responde=render(
        request=request,
        template_name='mysite/template1.html',
        context={},
    )
    return http_responde

def listar_estudiantes(request):
    contexto={
        "estudiantes":[
            {"nombre": "Daniel","apellido":"Marulanda"},
            {"nombre":"Natalia","apellido":"Marulanda"},
            {"nombre":"Guido","apellido":"Marulanda"},
            {"nombre":"Jacqueline","apellido":"Arce"}
        ]
    }
    http_responde=render(
       request=request,
template_name='control_estudios/lista_estudiantes.html',
context=contexto, 
    )
    return http_responde