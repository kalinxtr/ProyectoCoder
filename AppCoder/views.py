from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola Django - Coder")

def testingHTML(request):
    mi_html = open("C:/Users/nehue/Documents/Curso Python CoderHouse/Django/Proyecto1/AppCoder/templates/inicio.html")
    template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    doc = template.render(mi_contexto)

    return HttpResponse(doc)

def estudiantes_view(request):
    mi_html = open("C:/Users/nehue/Documents/Curso Python CoderHouse/Django/Proyecto1/AppCoder/templates/estudiantes.view.html")
    template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    doc = template.render(mi_contexto)

    return HttpResponse(doc)

def profesores_view(request):
    mi_html = open("C:/Users/nehue/Documents/Curso Python CoderHouse/Django/Proyecto1/AppCoder/templates/profesores.view.html")
    template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    doc = template.render(mi_contexto)

    return HttpResponse(doc)

def cursos_view(request):
    mi_html = open("C:/Users/nehue/Documents/Curso Python CoderHouse/Django/Proyecto1/AppCoder/templates/cursos.view.html")
    template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    doc = template.render(mi_contexto)

    return HttpResponse(doc)

def navbar_view(request):
    mi_html = open("C:/Users/nehue/Documents/Curso Python CoderHouse/Django/Proyecto1/AppCoder/templates/NavBar.html")
    template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    doc = template.render(mi_contexto)

    return HttpResponse(doc)

def entregables_view(request):
    mi_html = open("C:/Users/nehue/Documents/Curso Python CoderHouse/Django/Proyecto1/AppCoder/templates/entregables.view.html")
    template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    doc = template.render(mi_contexto)

    return HttpResponse(doc)

