




from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "reportes"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('reportes/', views.reportes, name='reportes'),
    path('1/', views.reporte1, name='reporte1'),
    path('2/', views.reporte2, name='reporte2'),
    path('3/', views.reporte3, name='reporte3'),
    path('4/', views.reporte4, name='reporte4'),
    path('5/', views.reporte5, name='reporte5'),
    path('6/', views.reporte6, name='reporte6'),
]
