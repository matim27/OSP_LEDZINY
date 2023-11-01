from django.conf.urls.static import static
from django.urls import path
from OSP_APP import settings
from depot_departure.views import DepotDepartureAddView

urlpatterns = [
    path('depot/add/', DepotDepartureAddView.as_view(), name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
