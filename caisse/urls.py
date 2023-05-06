from django.urls import path
from .views import flux,create_pro,update_O,delete_O,update_SoldeI,render_pdf_JC

urlpatterns = [
    path('', flux, name='flux'),
    path('createOperation/', create_pro, name='createOperation'),
    path('updOperation/<int:myid>', update_O, name='updOperation'),
    path('update_SoldeI/<int:myid>', update_SoldeI, name='update_SoldeI'),
    path('delete_O/<int:myid>',delete_O, name = "delete_O"),
    path('printcaisse',render_pdf_JC, name = "printcaisse"),
       
]