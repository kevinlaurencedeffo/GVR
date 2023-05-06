from django.urls import path
from .views import gstock, update_Art,delete_Art,detail_Art,create_Art,render_pdf_art

urlpatterns = [
    path('', gstock, name='gstock'),
    path('update_Art/<int:myid>', update_Art, name='update_Art'),
    path('create_Art/', create_Art, name='create_Art'),
    path('delete_Art/<int:myid>',delete_Art, name = "delete_Art"),
    path('detail_Art/<int:myid>',detail_Art, name = "detail_Art"),
    path('printart',render_pdf_art, name = "printart"),

]