from django.urls import path
from AppCoder.views import saludo, testingHTML, estudiantes_view, profesores_view, entregables_view, cursos_view

urlpatterns = [
    path("saludo/", saludo),
    path("",testingHTML),
    path("estudiante/",estudiantes_view),
    path("profesores/",profesores_view),
    path("cursos/",cursos_view),
    path("entregables/",entregables_view)

]