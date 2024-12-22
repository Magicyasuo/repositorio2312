from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import FUIDCreateView, FUIDUpdateView, lista_fuids
from django.urls import path
from .views import detalle_fuid
from .views import crear_ficha_paciente
from .views import lista_fichas_paciente
from .views import EditarFichaPaciente, detalle_ficha_paciente
from .views import ListaFichasAPIView
from .views import export_fuid_to_excel




# from .views import export_fuids_to_excel





urlpatterns = [
    path('', views.lista_registros, name='lista_registros'),  # Página principal de registros
    path('nuevo/', views.crear_registro, name='crear_registro'),
    path('<int:pk>/editar/', views.editar_registro, name='editar_registro'),
    path('<int:pk>/eliminar/', views.eliminar_registro, name='eliminar_registro'),
    path('cargar_subseries/', views.cargar_subseries, name='cargar_subseries'),
    path('cargar_series/', views.cargar_series, name='cargar_series'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registros/completo/', views.lista_completa_registros, name='lista_completa_registros'),
    path('fuids/', views.lista_fuids, name='lista_fuids'),
    # path('fuids/', lista_fuids, name='lista_fuids'),
    path('fuids/create/', FUIDCreateView.as_view(), name='crear_fuid'),
    path('fuids/edit/<int:pk>/', FUIDUpdateView.as_view(), name='editar_fuid'),
    path('fuids/detalle/<int:pk>/', detalle_fuid, name='detalle_fuid'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('crear-ficha/', crear_ficha_paciente, name='crear_ficha'),
    path('lista-fichas/', lista_fichas_paciente, name='lista_fichas'),
    path('editar-ficha/<int:consecutivo>/', EditarFichaPaciente.as_view(), name='editar_ficha'),
    path('detalle-ficha/<int:consecutivo>/', detalle_ficha_paciente, name='detalle_ficha'),
    path('api/lista-fichas/', ListaFichasAPIView.as_view(), name='api_lista_fichas'),
    path('fuid/<int:pk>/export-excel/', export_fuid_to_excel, name='export_fuid_to_excel'),






    
    


    # path('fuids/<int:fuid_id>/exportar/', exportar_fuid_excel, name='exportar_fuid_excel'),
    # path('export/fuids/', export_fuids_to_excel, name='export_fuids'),


   # path('login/', views.login_view, name='login'),
]
