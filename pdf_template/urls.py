from django.urls import path
from .views import POCListPDFViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register('generate-pdf', POCListPDFViewSet, basename='POCListPDFViewSet')


urlpatterns = [
   
]
