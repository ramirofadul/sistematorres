from rest_framework import serializers

from apps.juicios.models import TiposProcesos


class TiposProcesosSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiposProcesos
        exclude = ('state','created_date','modified_date','deleted_date')
