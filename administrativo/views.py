from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import *
from .serializers import EmprendimientoSerializers, EmprendedorSerializers,ServicioSerializers
from .models import Emprendimiento,Emprendedor,Servicio

################################################### INDEX ###################################################

class Index(View):

    def get(self,request):
        servicios=Servicio.objects.all()
        print(servicios)
        valor=[]
        for servicio in servicios:
            emprendimientos= Emprendimiento.objects.all().filter(servicio=servicio)
            valor.append(emprendimientos)
        


        return render(request, 'presentacion/index.html', {'servicios':servicios,'emprendimientos':emprendimientos,'valor':valor} )


################################################## Reserva ##################################################

class GenerarReserva(View):
    def get(self, request):
        return render(request, 'reservas/reserva.html', { })

###############################        Individual View         ################################

class ListarEmprendimientos(View):
    def get (self,request, id_servicio):
        servicios= Servicio.objects.all()
        if not id_servicio:
            id_servicio=1
        emprendimientos=Emprendimiento.objects.all().order_by('servicio').filter(servicio=id_servicio)
        print(emprendimientos)
        return render(request, 'emprendimiento/listaEmprendimientos.html',{'emprendimientos':emprendimientos,'servicios':servicios,} )

class VerEmprendimiento(View):
    def get(self, request, idEmprendimiento):
        emprendimiento=Emprendimiento.objects.all().filter(id=idEmprendimiento)
        form=ReservasForm()
        emprendimiento=emprendimiento
        return render(request,'emprendimiento/emprendimiento.html',{'form':form ,'emprendimiento':emprendimiento})

    def post(self, request, *args, **kwargs):
        form = ReservaFormulario(request.POST or None, request.FILES or None)
        valor= kwargs
        if form.is_valid():
            fechaReserva= form.cleaned_data['fechaReserva']
            emprendimiento= form.cleaned_data['emprendimiento']
            cantidad=form.cleaned_data['cantidad']
            valor= form.cleaned_data['valor']
            #productos=form.cleaned_data['productos']
            reserva= Reserva(
                fechaReserva=fechaReserva,
                emprendimiento=emprendimiento,
                cantidad=cantidad,
                valor=valor
            )
            reserva.save()
            form=ReservaFormulario()
            return HttpResponseRedirect("index")
        else:
            return render(request,'emprendimiento/emprendimiento.html',{'form':form})



class ListarServicios(View):
    def get (self,request):
        servicios= Servicio.objects.all().order_by('nombreS')
        return render(request, 'servicio/listarServicios.html',{'servicios':servicios})

class VerServicio(View):
    def get(self, request, idServicio):
        servicio=Emprendimiento.objects.all().filter(id=idServicio)
        servicio= Servicio.objects.all().filter(id=idServicio)

        return render(request,'servicio/servicio.html',{'servicio':servicio})





#################################### Servicios para aplicaciones Moviles ############################################
class Emprendedor_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        emprendedores= Emprendedor.objects.all()
        serializer= EmprendedorSerializers(emprendedores,many=True)    
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=EmprendedorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Emprendedor_APIView_Detalles(APIView):
    def get_object(self, emprendedor_id):
        try:
            return Emprendedor.objects.get(id=emprendedor_id)
        except Emprendedor.DoesNotExist:
            raise Http404

    def get(self,request,id_emprendedor,format=None):
        emprendedor = self.get_object(id_emprendedor)
        serializer= EmprendedorSerializers(emprendedor)
        return Response(serializer.data)

    def put(self,request,id_emprendedor, format=None):
        emprendedor=self.get_object(id_emprendedor)
        serializer= EmprendedorSerializers(emprendedor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Servicio_APIView(APIView):
    def get(self, request,format =None, *args, **Kwargs):
        servicio= Servicio.objects.all()
        serializer= ServicioSerializers(servicio,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=ServicioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Servicio_APIView_Detalles(APIView):

    def get_object(self, servicio_id):
        try:
            return Servicio.objects.get(id=servicio_id)
        except Servicio.DoesNotExist:
            raise Http404

    def get(self,request,id_servicio,format=None):
        servicio = self.get_object(id_servicio)
        serializer= ServicioSerializers(servicio)
        return Response(serializer.data)

    def put(self,request,id_servicio, format=None):
        servicio=self.get_object(id_servicio)
        serializer= ServicioSerializers(servicio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Emprendimiento_APIView(APIView):

    def get(self, request,format =None, *args, **Kwargs):

        emprendimientos = Emprendimiento.objects.all()
        serializer= EmprendimientoSerializers(emprendimientos,many=True)
        
        return Response(serializer.data)

    def post(self,request,format=None):

        serializer=EmprendimientoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    

class Emprendimiento_APIView_Detalles(APIView):
    #Obtener todos los objetos
    def get_object(self, emprendimiento_id):
        try:
            return Emprendimiento.objects.get(id=emprendimiento_id)
        except Emprendimiento.DoesNotExist:
            raise Http404


    #encontrar el objeto encontrado en el api
    def get(self,request,id_emprendimiento,format=None):
        emprendimiento = self.get_object(id_emprendimiento)
        serializer= EmprendimientoSerializers(emprendimiento)
        return Response(serializer.data)

    def put(self,request,id_emprendimineto, format=None):
        emprendimiento=self.get_object(id_emprendimineto)
        serializer= EmprendimientoSerializers(emprendimiento,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



