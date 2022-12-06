from django import forms
from .models import Reserva
# creating a form


class ReservasForm(forms.Form):
	class Meta:
		model=Reserva
		fields="__all__"


class ReservaFormulario(forms.ModelForm):
	class Meta:
		fields=[
			'fechaReserva',
			'emprendimiento',
			'cantidad',
			'valor'
		]

		labels={
			'fechaReserva':'Fecha de la reservacion',
			'emprendimiento':'Emprendimiento',
			'cantidad':'Cantidad del producto',
			'valor':'Costo'
		}
		widgets={
			'fechaReserva':forms.DateInput(format=('%d-%m-%y'),attrs={'type':'date'})
		}