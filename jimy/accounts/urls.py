from django.urls import path
from . import views,models


urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login, name ='login'),
    path('logout',views.logout, name ='logout'),
    path('change',views.change, name ='change'),
    path('pag_anadir',views.pag_anadir, name ='pag_anadir'),
    path('pag_eliminar',views.pag_eliminar, name ='pag_eliminar'),
    path('pag_modificar',views.pag_modificar, name ='pag_modificar'),
    ]