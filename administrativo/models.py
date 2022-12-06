from django.db import models
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE

class Rol(models.Model):

    nombre = models.CharField(verbose_name='Ingresar el nombre del rol', max_length=80, help_text='Ingrese el nombre del rol')
    descripcion = models.TextField(verbose_name='Ingrese una descrición detallada del rol', help_text='Descripcion del rol')

    class Meta:
        verbose_name = 'Permiso del sistema'
        verbose_name_plural = 'Permisos para usuarios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        permisos_defecto = ['add', 'change', 'delete', 'view']
        if not self.id:
            nuevo_grupo, creado = Group.objects.get_or_create(name=f'{self.nombre}')
            for permiso_temp in permisos_defecto:
                permiso, creado = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.nombre} ',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.nombre}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args, **kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id=self.id).values('nombre').first()
            if rol_antiguo['nombre'] == self.nombre:
                super().save(*args, **kwargs)
            else:
                Group.objects.filter(name=rol_antiguo['nombre'].update(name=f'{self.nombre}'))
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename=f"{permiso_temp}_{rol_antiguo['nombre']}").update(
                        codename = f'{permiso_temp}_{self.nombre}',
                        name= f'Can {permiso_temp} {self.nombre}'
                    )
                super().save(*args, **kwargs)

class Persona(models.Model):

    TIPO_DOCUMENTO_CHOICE = [
        ('cedula', 'Cedula'),
        ('pasaporte', 'Pasaporte'),
    ]

    tipoDocumento = models.CharField(verbose_name="Tipo de documento", max_length=20, choices=TIPO_DOCUMENTO_CHOICE)
    cedula= models.CharField(verbose_name="Cedula",max_length=13)
    nombre= models.CharField(verbose_name="Nombres",max_length= 100 )
    apellido = models.CharField( verbose_name= "Apellidos", max_length= 100)
    origin= models.CharField(verbose_name="Nacionalidad", max_length= 100)
    correo= models.EmailField(verbose_name="Correo Electronico")
    celular= models.CharField(verbose_name="Numero de celular",max_length=13)
    
    def duplicidadCedula(self):
        persona= persona.objects.all() 
        for persona in persona:
            if persona.cedula == self.cedula:
                print("Existe la cedula")
                self.nombre= persona.nombre
            else:
                print("La cedula no coincide")


    def __str__(self):
        return self.cedula

class Servicio(models.Model):

    nombreS = models.CharField(verbose_name="Nombre del Servicio", max_length=100,blank=True, null=True)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=500)
    foto = models.ImageField(upload_to="fotoCategoria/", verbose_name="Foto del servicio", null = True, blank=True)

    def __str__(self) -> str:
        return self.nombreS

class Video(models.Model):

    nombreVideo= models.CharField(max_length=255,blank=True,null=True)
    urlVideo= models.URLField(max_length=255)

class Foto(models.Model):

    nombreFoto=models.CharField(max_length=255,blank=True,null=True)
    urlFoto= models.ImageField(upload_to="fotoNegocio/", verbose_name="Imagen del negocio", null = True, blank=True)
 
class Producto(models.Model):

    foto=models.ImageField(upload_to="fotoProducto/", verbose_name="Foto del Producto", null = True, blank=True)
    nombreP= models.CharField(verbose_name="Nombre del producto", max_length=100)
    descripcion= models.CharField(verbose_name="Descripcion",max_length=200)
    cantidad= models.IntegerField(blank=True,null=True)
    precio= models.DecimalField(max_digits=10, decimal_places=2)

class Administrador(Persona):

    estado_Choice=[
        ('ACTIVO','Activo'),('INACTIVO','Inactivo')
    ]

    rol= models.OneToOneField(Rol,verbose_name="Rol_Administrador", on_delete=models.RESTRICT)
    usuario = models.OneToOneField(User, on_delete=CASCADE, blank=True, null=True)
    fechaInicio= models.DateTimeField(blank=True, null=True)
    fechaActualizacion = models.DateTimeField(blank=True, null=True)
    estado= models.CharField(choices=estado_Choice,max_length=20,blank=True, null=True)

class Cliente(Persona):

    direccion= models.CharField(verbose_name="Direccion", max_length=100)  
  
class Emprendimiento(models.Model):

    ruc=models.CharField(verbose_name="RUC de la empresa",max_length=11,blank=True, null=True,)
    nombreEmprendimiento = models.CharField(verbose_name ="Nombre del emprendimiento",max_length=200)
    direccion = models.CharField(verbose_name="Direccion del Emprendimiento",max_length=200)
    telCelular= models.CharField(verbose_name= "celular",max_length= 13)
    telFijo= models.CharField(verbose_name= "Telf. Fijo",max_length= 13)
    descripcion=models.TextField()
    horaApertura=models.DateTimeField()
    horaCierre=models.DateTimeField()
    altitud= models.CharField(verbose_name="altitud", max_length=20)
    latitud= models.CharField(verbose_name="latitud", max_length=20)
    servicio=models.ForeignKey(Servicio, verbose_name='Servicios', on_delete=models.CASCADE)
    foto= models.ManyToManyField(Foto,verbose_name="Fotos del negocio", blank=True, null=True)
    video= models.ManyToManyField(Video,verbose_name="Videos del negocio",blank=True, null=True)
    instagram= models.URLField(verbose_name="Instagram", blank=True, null=True)
    facebook= models.URLField(verbose_name="Facebook", blank=True, null=True)
    productos= models.ManyToManyField(Producto, verbose_name='Productos')
    class Meta:
        verbose_name= "Emprendimiento"
        verbose_name_plural= "Emprendimientos"

    def __str__(self) -> str:
        return self.nombreEmprendimiento

class Emprendedor(Persona):

    emprendimientos= models.ManyToManyField(Emprendimiento,blank=True)

    class Meta:
        verbose_name = "Personas que emprenden"
        verbose_name_plural ="Emprendedores (personas)"

class Reserva(models.Model):
    
    fechaReserva=models.DateTimeField(verbose_name="Fecha a la que se reserva",)
    cantidad=models.IntegerField(verbose_name="Tipo de emprendimiento")
    emprendimiento= models.ForeignKey(Emprendimiento,on_delete=models.PROTECT,blank=True, null=True)
    valor= models.FloatField()
    producto=models.ManyToManyField(Producto,verbose_name="Producto a reservar")