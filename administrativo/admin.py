from django.contrib import admin
from django.db import models


from .models import Rol,Servicio,Emprendedor,Emprendimiento,Administrador,Producto,Foto,Video,Cliente


class EmprendedorAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido',)
    search_fields = ('cedula','nombre', 'apellido', )
    list_filter = ('cedula',)
    ordering = ('cedula', 'nombre','apellido',)
    fieldsets =(

        ('Informacion Personal', {
            'fields': ('nombre', 'apellido','tipoDocumento' 'cedula','origin',)
        }),
        ('Informacion de contacto', {
            'fields': ('celular', 'dirrecion','correo',)
        }),
        ('Informacion de Emprendimientos', {
            'fields': ('emprendimiento',)
        }),
    )

class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ('ruc','nombreEmprendimiento',)
    search_fields = ('ruc','nombreEmprendimiento', )
    list_filter = ('ruc',)
    ordering = ('ruc','nombreEmprendimiento',)
    fieldsets =(

        ('Informacion sobre la empresa', {
            'fields': ('ruc', 'nombreEmprendimiento','descripcion' ,'servicio','video','foto')
        }),
        ('Informacion de ubicacion', {
            'fields': ('direccion', 'latitud','altitud',)
        }),
        ('Informacion de contacto ', {
            'fields': ('telFijo', 'telCelular',)
        }),
        ('Horarios de atencion', {
            'fields': ('horaApertura', 'horaCierre',)
        }),
        ('Redes Sociales', {
            'fields': ('instagram', 'facebook',)
        }),
    )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido',)
    search_fields = ('cedula','nombre', 'apellido', )
    list_filter = ('cedula',)
    ordering = ('cedula','apellido', 'nombre',)
    fieldsets =(

        ('Informacion Personal', {
            'fields': ('nombre', 'apellido','tipoDocumento' 'cedula','origin',)
        }),
        ('Informacion de contacto', {
            'fields': ('celular', 'dirrecion','correo','direccion')
        }),
    )

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido',)
    search_fields = ('cedula','nombre', 'apellido', )
    list_filter = ('cedula',)
    ordering = ('cedula','apellido', 'nombre',)
    fieldsets =(

        ('Informacion Personal', {
            'fields': ('nombre', 'apellido','tipoDocumento' 'cedula','origin','usuario')
        }),
        ('Informacion de contacto', {
            'fields': ('celular', 'dirrecion','correo',)
        }),
        ('Permisos', {
            'fields': ('estado', '','rol','fechaInicio','fechaActualizacion')
        }),    
    
    )


admin.site.index_title = "Bienvenidos al portal de Administración. "
admin.site.register(Servicio)
admin.site.register(Emprendedor,EmprendedorAdmin)
admin.site.register(Emprendimiento,EmprendimientoAdmin)
admin.site.register(Administrador,AdministradorAdmin)
admin.site.register(Producto)
admin.site.register(Rol)
admin.site.register(Foto)
admin.site.register(Video)
admin.site.register(Cliente,ClienteAdmin)