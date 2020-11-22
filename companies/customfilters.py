from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter
from companies.models import Profession, Employee, Company, PartnerShip

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


class PartnerShipFilter(FilterSet):
	"""
	Filter class for partnership model
	"""

	from_year_partnership = DateTimeFilter(field_name='year_partnership', lookup_expr='gte')
	to_year_partnership = DateTimeFilter(field_name='year_partnership', lookup_expr='lte')
	company_inviter_name = AllValuesFilter(field_name='company_inviter__name')

	class Meta:
		model = PartnerShip
		fields = (
			# company_inviter__name will be accessed as company_inviter_name
			'company_inviter_name',
			'year_partnership',
			'from_year_partnership',
			'to_year_partnership',
		)
