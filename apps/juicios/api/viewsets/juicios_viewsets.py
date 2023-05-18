from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


from apps.base.utils import validate_files
from apps.juicios.api.serializers.juicios_serializers import (
    JuiciosSerializer, JuiciosRetrieveSerializer
)

class JuiciosViewSet(viewsets.ModelViewSet):
    serializer_class = JuiciosSerializer
    parser_classes = (JSONParser, MultiPartParser, )
#    renderer_classes = [TemplateHTMLRenderer]
#    template_name = '.html'

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        juicios_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": juicios_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer 
        data = request.data
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Juicio creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = JuiciosRetrieveSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un juicio con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            data = request.data
            juicios_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if juicios_serializer.is_valid():
                juicios_serializer.save()
                return Response({'message':'Juicio actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':juicios_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        juicio = self.get_queryset().filter(id=pk).first() # get instance        
        if juicio:
            juicio.state = False
            juicio.save()
            return Response({'message':'Juicio eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Juicio con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
