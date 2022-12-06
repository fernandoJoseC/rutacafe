# Generated by Django 4.1.3 on 2022-12-01 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Foto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombreFoto", models.CharField(blank=True, max_length=255, null=True)),
                ("urlFoto", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipoDocumento",
                    models.CharField(
                        choices=[("cedula", "Cedula"), ("pasaporte", "Pasaporte")],
                        max_length=20,
                        verbose_name="Tipo de documento",
                    ),
                ),
                ("cedula", models.CharField(max_length=13, verbose_name="Cedula")),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombres")),
                (
                    "apellido",
                    models.CharField(max_length=100, verbose_name="Apellidos"),
                ),
                (
                    "origin",
                    models.CharField(max_length=100, verbose_name="Nacionalidad"),
                ),
                (
                    "correo",
                    models.EmailField(
                        max_length=254, verbose_name="Correo Electronico"
                    ),
                ),
                (
                    "celular",
                    models.CharField(max_length=13, verbose_name="Numero de celular"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "foto",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="fotoProducto",
                        verbose_name="Foto del Producto",
                    ),
                ),
                (
                    "nombreP",
                    models.CharField(
                        max_length=100, verbose_name="Nombre del producto"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(max_length=200, verbose_name="Descripcion"),
                ),
                ("cantidad", models.IntegerField(blank=True, null=True)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        help_text="Ingrese el nombre del rol",
                        max_length=80,
                        verbose_name="Ingresar el nombre del rol",
                    ),
                ),
                (
                    "descripcion",
                    models.TextField(
                        help_text="Descripcion del rol",
                        verbose_name="Ingrese una descrición detallada del rol",
                    ),
                ),
            ],
            options={
                "verbose_name": "Permiso del sistema",
                "verbose_name_plural": "Permisos para usuarios",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombreS",
                    models.CharField(
                        choices=[
                            ("ventaProductos", "Venta de productos"),
                            ("servicioRestaurante", "Alojamiento"),
                            ("produccionProductos", "Produccion de productos"),
                            ("atractivoTuristico", "Atractivo Turistico"),
                            ("hospedaje", "Hospedaje"),
                            ("cafeteria", "Cafeteria"),
                            ("piscina", "Piscina"),
                            ("camping", "Camping"),
                            ("caminata", "Caminata"),
                            ("cabalgata", "Cabalgata"),
                            ("recreacion", "Recreacion"),
                            ("comidaTipica", "Comida Tipica"),
                            ("comidaRapida", "Comida Rapida"),
                            ("comidaCoreana", "Comida Coreana"),
                        ],
                        max_length=100,
                        verbose_name="Nombre del Servicio",
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(max_length=500, verbose_name="Descripcion"),
                ),
                (
                    "foto",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="fotoCategoria",
                        verbose_name="Foto del servicio",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombreVideo",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("urlVideo", models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="administrativo.persona",
                    ),
                ),
                (
                    "direccion",
                    models.CharField(max_length=100, verbose_name="Direccion"),
                ),
            ],
            bases=("administrativo.persona",),
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "productos",
                    models.ManyToManyField(
                        to="administrativo.producto", verbose_name="Productos"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Emprendimiento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ruc",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        verbose_name="RUC de la empresa",
                    ),
                ),
                (
                    "nombreEmprendimiento",
                    models.CharField(
                        max_length=200, verbose_name="Nombre del emprendimiento"
                    ),
                ),
                (
                    "direccion",
                    models.CharField(
                        max_length=200, verbose_name="Direccion del Emprendimiento"
                    ),
                ),
                ("telCelular", models.CharField(max_length=13, verbose_name="celular")),
                ("telFijo", models.CharField(max_length=13, verbose_name="Telf. Fijo")),
                ("descripcion", models.TextField()),
                ("horaApertura", models.DateTimeField()),
                ("horaCierre", models.DateTimeField()),
                ("altitud", models.CharField(max_length=20, verbose_name="altitud")),
                ("latitud", models.CharField(max_length=20, verbose_name="latitud")),
                (
                    "instagram",
                    models.URLField(blank=True, null=True, verbose_name="Instagram"),
                ),
                (
                    "facebook",
                    models.URLField(blank=True, null=True, verbose_name="Facebook"),
                ),
                (
                    "foto",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        to="administrativo.foto",
                        verbose_name="Fotos del negocio",
                    ),
                ),
                (
                    "menu",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrativo.menu",
                        verbose_name="Productos del restaurante=",
                    ),
                ),
                (
                    "servicio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrativo.servicio",
                        verbose_name="Servicios",
                    ),
                ),
                (
                    "video",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        to="administrativo.video",
                        verbose_name="Videos del negocio",
                    ),
                ),
            ],
            options={
                "verbose_name": "Emprendimiento",
                "verbose_name_plural": "Emprendimientos",
            },
        ),
        migrations.CreateModel(
            name="Emprendedor",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="administrativo.persona",
                    ),
                ),
                (
                    "emprendimientos",
                    models.ManyToManyField(
                        blank=True, to="administrativo.emprendimiento"
                    ),
                ),
            ],
            options={
                "verbose_name": "Personas que emprenden",
                "verbose_name_plural": "Emprendedores (personas)",
            },
            bases=("administrativo.persona",),
        ),
        migrations.CreateModel(
            name="Administrador",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="administrativo.persona",
                    ),
                ),
                ("fechaInicio", models.DateTimeField(blank=True, null=True)),
                ("fechaActualizacion", models.DateTimeField(blank=True, null=True)),
                (
                    "estado",
                    models.CharField(
                        blank=True,
                        choices=[("ACTIVO", "Activo"), ("INACTIVO", "Inactivo")],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "rol",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="administrativo.rol",
                        verbose_name="Rol_Administrador",
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("administrativo.persona",),
        ),
    ]
