from rest_framework import viewsets, mixins, generics
from companies.customfilters import ProfessionFilter, EmployeeFilter, CompanyFilter, PartnerShipFilter
from companies.models import Profession, Employee, Company, PartnerShip
from companies.serializers import (ProfessionSerializer, DetailProfessionSerializer, EmployeeSerializer, PartnerShipSerializer,
								 DetailPartnerShipSerializer, DetailEmployeeSerializer, CompanySerializer, DetailCompanySerializer)


class ProfessionViewSet(viewsets.ModelViewSet):
	"""
	ViewSet for profession model
	"""

	queryset = Profession.objects.all()

	filter_class = ProfessionFilter
	search_fields = (
			'^name',
		)
	ordering_fields = (
			'name',
		)

	def get_serializer_class(self):
		if hasattr(self, 'action') and self.action == 'list':
			return 	ProfessionSerializer

		return DetailProfessionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
	"""
	ViewSet for employee model
	"""

	queryset = 	Employee.objects.all()

	filter_class = EmployeeFilter
	search_fields = (
			'^name',
		)
	ordering_fields = (
			'name',
			'age',
			'profession__name',
			'company__name',
			'salary',
			'hired_date',
			'promotion_date',
		)

	def get_serializer_class(self):
		if hasattr(self, 'action') and self.action == 'list':
			return 	EmployeeSerializer
		
		return DetailEmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
	"""
	ViewSet for company model
	"""

	queryset = 	Company.objects.all()

	filter_class = CompanyFilter
	search_fields = (
			'^name',
			'^type_of_company',
			'^country'
		)
	ordering_fields = (
			'name',
			'year_of_foundation',
		)

	def get_serializer_class(self):
		if hasattr(self, 'action') and self.action == 'list':
			return 	CompanySerializer

		return DetailCompanySerializer


class PartnerShipView(mixins.ListModelMixin,
					  mixins.RetrieveModelMixin,
					  mixins.UpdateModelMixin,
					  viewsets.GenericViewSet):

	queryset = PartnerShip.objects.all()

	filter_class = PartnerShipFilter
	search_fields = (
			'^company_inviter__name',
			'^joint_products'
		)
	ordering_fields = (
			'year_partnership',
		)

	def get_serializer_class(self):
		if hasattr(self, 'action') and self.action == 'list':
			return 	PartnerShipSerializer

		return DetailPartnerShipSerializer