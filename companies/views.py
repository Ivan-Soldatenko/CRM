from rest_framework import viewsets, mixins, generics
from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter

from companies.models import Profession, Employee, Company, PartnerShip
from companies.serializers import (ProfessionSerializer, DetailProfessionSerializer, EmployeeSerializer, PartnerShipSerializer,
								 DetailPartnerShipSerializer, DetailEmployeeSerializer, CompanySerializer, DetailCompanySerializer)


class EmployeeFilter(FilterSet):
	"""
	Filter class for employee model
	"""

	from_hired_date = DateTimeFilter(field_name='hired_date', lookup_expr='gte')
	to_hired_date = DateTimeFilter(field_name='hired_date', lookup_expr='lte')
	from_promotion_date = DateTimeFilter(field_name='promotion_date', lookup_expr='gte')
	to_promotion_date = DateTimeFilter(field_name='promotion_date', lookup_expr='lte')
	min_salary = NumberFilter(field_name='salary', lookup_expr='gte')
	max_salary = NumberFilter(field_name='salary', lookup_expr='lte')
	min_age = NumberFilter(field_name='age', lookup_expr='gte')
	max_age = NumberFilter(field_name='age', lookup_expr='lte')
	profession_name = AllValuesFilter(field_name='profession__name')
	company_name = AllValuesFilter(field_name='company__name')

	class Meta:
		model = Employee
		fields = (
			'name',
			'gender',
			'age',
			'min_age',
			'max_age',
			'hired_date',
			'from_hired_date',
			'to_hired_date',
			'promotion_date',
			'from_promotion_date',
			'to_promotion_date',
			'salary',
			'min_salary',
			'max_salary',
			# profession__name will be accessed as profession_name
			'profession_name',
			# company__name will be accessed as company_name
			'company_name',
	 	)


class CompanyFilter(FilterSet):
	"""
	Filter class for company model
	"""

	from_year_of_foundation = DateTimeFilter(field_name='year_of_foundation', lookup_expr='gte')
	to_year_of_foundation = DateTimeFilter(field_name='year_of_foundation', lookup_expr='lte')

	class Meta:
		model = Company
		fields = (
			'name',
			'type_of_company',
			'country',
			'year_of_foundation',
			'from_year_of_foundation',
			'to_year_of_foundation',
	 	)


class ProfessionViewSet(viewsets.ModelViewSet):
	"""
	ViewSet for profession model
	"""

	queryset = Profession.objects.all()

	filter_fields = (
			'name',
		)
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

	def get_serializer_class(self):
		if hasattr(self, 'action') and self.action == 'list':
			return 	PartnerShipSerializer

		return DetailPartnerShipSerializer