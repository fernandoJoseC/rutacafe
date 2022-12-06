# Generated by Django 4.1.3 on 2022-12-02 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrativo", "0002_reserva_remove_emprendimiento_menu_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="emprendimiento",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="administrativo.emprendimiento",
            ),
        ),
    ]