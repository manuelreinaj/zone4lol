from django.urls import path
from foro.views import *


urlpatterns = [
#Paths de Foros
    path('foros/listar', forosList.as_view(), name='foros_listar'),
    path('foros/nuevo', foroCreate.as_view(), name='foro_crear'),
    path('foros/eliminar/<pk>', foroDelete.as_view(), name='foro_eliminar'),
    path('foros/foro/<pk>', postForo, name='posts_listar'),
    path('foros/post/nuevo/<pk>', postCreate, name='post_crear'),
    path('foros/post/eliminar/<pk>', postDelete.as_view(), name='post_eliminar'),
]