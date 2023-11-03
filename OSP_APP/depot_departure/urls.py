from django.conf.urls.static import static
from django.urls import path
from OSP_APP import settings
from depot_departure.views import DepotDepartureAddView, DepotDepartureListView

urlpatterns = [
    path('depot/add/', DepotDepartureAddView.as_view(), name='depot_add'),
    path('depot/list/', DepotDepartureListView.as_view(), name='depot_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
