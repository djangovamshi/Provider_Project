from django.urls import path,include
from Provider_App.api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees',views.Employee_ModelViewSet)

urlpatterns =[
    path('',include(router.urls)),
]