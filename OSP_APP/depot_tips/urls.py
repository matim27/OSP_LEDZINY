from django.conf.urls.static import static
from django.urls import path
from OSP_APP import settings
from depot_tips.views import DepotTipsView, DepotTipAddView, DepotTipImageAddView

urlpatterns = [
    path('depot_tips/list/', DepotTipsView.as_view(), name='depot_tips'),
    path('depot_tips/add/', DepotTipAddView.as_view(), name='depot_tip_add'),
    path('depot_tips/image/add/', DepotTipImageAddView.as_view(), name='depot_tip_image_add'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

