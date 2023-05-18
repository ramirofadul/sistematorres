from rest_framework import serializers

from apps.juicios.models import Juicios
from apps.juicios.api.serializers.general_serializers import (
    TiposProcesosSerializer
)

class JuiciosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Juicios
        exclude = ('state','created_date','modified_date','deleted_date')


class JuiciosRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juicios
        exclude = ('state','created_date','modified_date','deleted_date')