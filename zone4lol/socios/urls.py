from django.urls import path
from socios.views import *

from registration.views import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView

urlpatterns= [
# Paths de Socios
    path('socios/nuevo', socioCreate.as_view(), name='socio_crear'),
    path('socios/listar', staff_member_required(socioList.as_view(), login_url='usuario_login'), name='socios_listar'),
    path('socios/editar/<pk>', updateUser.as_view(), name='socio_editar'),
    path('socios/eliminar/<pk>', deleteUser.as_view(), name='socio_eliminar'),
    path('socio/detalle/<pk>', detalleUser.as_view(), name='socio_detalle'),

    # Paths de Users
    path('usuario/signup', userRegister.as_view(), name='usuario_signup'),
    path('usuario/login', LoginView.as_view(template_name='registrations/login.html'), name='usuario_login'),
    path('usuario/logout', LogoutView.as_view(next_page='registrations/login.html'), name='usuario_logout'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registrations/password_reset_form.html',
                                                           html_email_template_name='registrations/password_reset_email.html'),
         name="password_reset"),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registrations/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
         name='password_reset_complete'),
    ]