from django.urls import path
from .views import grh, create_Pers,create_Task,render_pdf_Pers, update_Pers,update_Task, delete_Pers,delete_Task, detail_Pers

urlpatterns = [
    path('', grh, name='grh'),
    path('create_Pers/', create_Pers, name='create_Pers'),
    path('create_Task/', create_Task, name='create_Task'),
    path('update_Pers/<int:myid>', update_Pers, name='update_Pers'),
    path('update_Task/<int:myid>', update_Task, name='update_Task'),
    path('delete_Pers/<int:myid>',delete_Pers, name = "delete_Pers"),
    path('delete_Task/<int:myid>',delete_Task, name = "delete_Task"),
    path('detail_Pers/<int:myid>',detail_Pers, name = "detail_Pers"),
    path('printpers',render_pdf_Pers, name = "printpers"),
    
]