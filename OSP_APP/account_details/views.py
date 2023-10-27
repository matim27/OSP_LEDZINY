from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from account_details.forms import DriverLicenseForm, MedicalCheckupForm, SmokeBoxForm, TrainingForm, UserEditForm
from account_details.models import DriverLicense, MedicalCheckup, SmokeBox, Training
from accounts.forms import UserForm

UserModel = get_user_model()


class AccountDetailsView(DetailView):
    model = UserModel
    template_name = 'account_details/account_details/account_details.html'
    context_object_name = 'user'

    def get_queryset(self):
        return UserModel.objects.filter(pk=self.request.user.pk)


# class AddDriverLicenseView(CreateView):
#     form_class = DriverLicenseForm
#     model = DriverLicense
#     # success_url = reverse_lazy('profile')
#     success_url = reverse_lazy('home')
#     template_name = 'account_details/driver_license/add_driver_license.html'
#
#     def form_valid(self, form):
#         existing_license = DriverLicense.objects.filter(
#             user=self.request.user,
#         )
#         if existing_license:
#             return render(self.request, 'account_details/messeges/add_driver_license_error.html')
#         else:
#             form.instance.user = self.request.user
#             return super().form_valid(form)


class EditDriverLicenseView(UpdateView):
    form_class = DriverLicenseForm
    model = DriverLicense
    template_name = 'account_details/driver_license/edit_driver_license.html'

    def get_success_url(self):
        return reverse_lazy('account_details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        driver_license, created = DriverLicense.objects.get_or_create(user=self.request.user)
        return driver_license


# class AddMedicalCheckupView(CreateView):
#     form_class = MedicalCheckupForm
#     model = MedicalCheckup
#     success_url = reverse_lazy('home')
#     template_name = 'account_details/medical_checkup/add_medical_checkup.html'
#
#     def form_valid(self, form):
#         existing_medical_checkup = MedicalCheckup.objects.filter(
#             user=self.request.user,
#         )
#         if existing_medical_checkup:
#             return render(self.request, 'account_details/messeges/add_medical_checkup_error.html')
#         else:
#             form.instance.user = self.request.user
#             return super().form_valid(form)


class EditMedicalCheckupView(UpdateView):
    form_class = MedicalCheckupForm
    model = MedicalCheckup
    template_name = 'account_details/medical_checkup/edit_medical_checkup.html'

    def get_success_url(self):
        return reverse_lazy('account_details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        medical_checkup, created = MedicalCheckup.objects.get_or_create(user=self.request.user)
        return medical_checkup


# class AddSmokeBoxView(CreateView):
#     form_class = SmokeBoxForm
#     model = SmokeBox
#     success_url = reverse_lazy('home')
#     template_name = 'account_details/smokebox/add_smokebox.html'
#
#     def form_valid(self, form):
#         existing_smokebox = SmokeBox.objects.filter(
#             user=self.request.user,
#         )
#         if existing_smokebox:
#             return render(self.request, 'account_details/messeges/add_smokebox_error.html')
#         else:
#             form.instance.user = self.request.user
#             return super().form_valid(form)


class EditSmokeBoxView(UpdateView):
    form_class = SmokeBoxForm
    model = SmokeBox
    template_name = 'account_details/smokebox/edit_smokebox.html'

    def get_success_url(self):
        return reverse_lazy('account_details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        smokebox, created = SmokeBox.objects.get_or_create(user=self.request.user)
        return smokebox


# class AddTrainingView(CreateView):
#     form_class = TrainingForm
#     model = Training
#     success_url = reverse_lazy('home')
#     template_name = 'account_details/training/add_training.html'
#
#     def form_valid(self, form):
#         existing_training = Training.objects.filter(
#             user=self.request.user,
#         )
#         if existing_training:
#             return render(self.request, 'account_details/messeges/add_training_error.html')
#         else:
#             form.instance.user = self.request.user
#             return super().form_valid(form)


class EditTrainingView(UpdateView):
    form_class = TrainingForm
    model = Training
    template_name = 'account_details/training/edit_training.html'

    def get_success_url(self):
        return reverse_lazy('account_details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        training, _ = Training.objects.get_or_create(user=self.request.user)
        return training


class AccountEditView(View):
    def get(self, request, *args, **kwargs):
        user = request.user

        form1 = UserEditForm(instance=UserModel.objects.get(pk=request.user.pk))
        driver_license, created2 = DriverLicense.objects.get_or_create(user=user)
        form2 = DriverLicenseForm(instance=driver_license)
        medical_checkup, created3 = MedicalCheckup.objects.get_or_create(user=user)
        form3 = MedicalCheckupForm(instance=medical_checkup)
        smoke_box, created4 = SmokeBox.objects.get_or_create(user=user)
        form4 = SmokeBoxForm(instance=smoke_box)

        return render(request, 'account_details/account_edit.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

    def post(self, request, *args, **kwargs):
        user = request.user

        form1 = UserEditForm(request.POST, instance=user)
        driver_license, created2 = DriverLicense.objects.get_or_create(user=user)
        form2 = DriverLicenseForm(request.POST, instance=driver_license)
        medical_checkup, created3 = MedicalCheckup.objects.get_or_create(user=user)
        form3 = MedicalCheckupForm(request.POST, instance=medical_checkup)
        smoke_box, created4 = SmokeBox.objects.get_or_create(user=user)
        form4 = SmokeBoxForm(request.POST, instance=smoke_box)

        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            return redirect('account_details', pk=user.pk)

        return render(request, 'account_details/account_edit.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})


class AccountListView(ListView):
    model = UserModel
    template_name = 'account_details/accounts_list/accounts_list.html'
    context_object_name = 'users'

