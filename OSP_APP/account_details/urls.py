from django.conf.urls.static import static
from django.urls import path
from OSP_APP import settings
from account_details.views import (EditDriverLicenseView, EditMedicalCheckupView, EditSmokeBoxView,
                                   EditTrainingView, AccountEditView, AccountListView, AccountDetailsView)

urlpatterns = [
    # path('user/driver/license/add/', AddDriverLicenseView.as_view(), name='add_driver_license'),
    path('user/driver/license/<int:pk>/', EditDriverLicenseView.as_view(), name='edit_driver_license'),
    # path('user/medical/checkup/add/', AddMedicalCheckupView.as_view(), name='add_medical_checkup'),
    path('user/medical/checkup/<int:pk>/', EditMedicalCheckupView.as_view(), name='edit_medical_checkup'),
    # path('user/smokebox/add/', AddSmokeBoxView.as_view(), name='add_smokebox'),
    path('user/smokebox/<int:pk>/', EditSmokeBoxView.as_view(), name='edit_smokebox'),
    # path('user/training/add/', AddTrainingView.as_view(), name='add_training'),
    path('user/training/<int:pk>/', EditTrainingView.as_view(), name='edit_training'),
    path('user/<int:pk>/details/', AccountDetailsView.as_view(), name='account_details'),
    path('user/edit/', AccountEditView.as_view(), name='account_edit'),
    path('users/list/', AccountListView.as_view(), name='account_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)