
from django.urls import path
from eventos.views import *


urlpatterns= [
    # Paths de Eventos
    # path('evento/listar', eventosList.as_view(), name='eventos_listar'),
    path('evento/listar', eventos_lista, name='eventos_listar'),
    path('evento/nuevo', eventoCreate.as_view(), name='evento_crear'),
    path('evento/editar/<pk>', eventoUpdate.as_view(), name='evento_editar'),
    path('evento/eliminar/<pk>', eventoDelete.as_view(), name='evento_eliminar'),
    ]