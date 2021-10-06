from django.shortcuts import render

# Create your views here.
from Provider_App.models import Employee
from Provider_App.forms import EmployeeForm
from django.views.generic import (
    ListView,DetailView,UpdateView,DeleteView,CreateView
)

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employee_list'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee/employee_form.html'
    context_object_name = 'form'


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee/employee_form.html'
    context_object_name = 'form'


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employees/'
    template_name = 'employee/employee_confirm_delete.html'
    context_object_name = 'employee'