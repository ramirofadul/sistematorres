from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.juicios.models import TiposProcesos
from apps.juicios.api.serializers.general_serializers import (
    TiposProcesosSerializer
)

class TiposProcesosUnitViewSet(viewsets.GenericViewSet):
    model = TiposProcesos
    serializer_class = TiposProcesosSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_tipos_procesos(self, request):
        data = TiposProcesos.objects.filter(state=True)
        data = TiposProcesosSerializer(data, many=True)
        return Response(data.data)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Tipo Proceso registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Tipo Proceso no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Tipo Proceso actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Tipo Proceso eliminado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Tipo Proceso no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)
