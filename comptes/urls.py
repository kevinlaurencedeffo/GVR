from django.urls import path
from .views import login_view, register,accounts,delete_User,administrateur,update_User,update_Me,anonimous,Logout
from django.contrib.auth import views
from API import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('logout/', Logout, name='Logout'),
    path('accounts', accounts, name='accounts'),
    path('update_Me/<int:myid>', update_Me, name='update_Me'),
    path('stocks/update_Me/<int:myid>', update_Me, name='update_Me'),
    path('personnel/update_Me/<int:myid>', update_Me, name='update_Me'),
    path('caisse/update_Me/<int:myid>', update_Me, name='update_Me'),
    path('update_User/<int:myid>', update_User, name='update_User'),
    path('delete_User/<int:myid>', delete_User, name='delete_User'),
    path('admins', administrateur, name='administrateur'),
    path('anonimous/', anonimous, name='anonimous'),
    path('reset_password',views.PasswordResetView.as_view(template_name='comptes/password_reset.html'), name='reset_password'),
    path('reset_password_send',views.PasswordResetDoneView.as_view(template_name='comptes/password_reset_send.html'), name="password_reset_done" ),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='comptes/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='comptes/password_reset_done.html'), name="password_reset_complete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)