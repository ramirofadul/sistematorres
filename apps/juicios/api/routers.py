from rest_framework.routers import DefaultRouter
from apps.juicios.api.viewsets.general_views import *
from apps.juicios.api.viewsets.juicios_viewsets import JuiciosViewSet

router = DefaultRouter()

router.register(r'juicios',JuiciosViewSet,basename = 'juicios')

urlpatterns = router.urls