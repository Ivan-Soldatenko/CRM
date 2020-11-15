from django.urls import path
from rest_framework.routers import DefaultRouter
from companies import views


app_name = "companies"
router = DefaultRouter()
# urls for profession ViewSet
router.register('professions', views.ProfessionViewSet, basename='profession')
# urls for employee ViewSet
router.register('employees', views.EmployeeViewSet, basename='employee')
# urls for company ViewSet
router.register('companies', views.CompanyViewSet, basename='company')

urlpatterns = router.urls 