from Provider_App.models import Employee
from Provider_App.api.serializers import EmployeeSerializer
from rest_framework import viewsets

class Employee_ModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

