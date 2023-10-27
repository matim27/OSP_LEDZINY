from django.conf.urls.static import static
from django.urls import path
from OSP_APP import settings
from fire_vehicle.views import GCBAView

urlpatterns = [
    path('vehicle/gcba/', GCBAView.as_view(), name='gcba'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)