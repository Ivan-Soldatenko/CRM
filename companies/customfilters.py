from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter
from companies.models import Profession, Employee, Company, PartnerShip
from django.db.models import Count


class ProfessionFilter(FilterSet):
	"""
	Filter class for profession model
	"""
	number_of_employees = NumberFilter(field_name='number_of_employees', method='filter_number_of_employee_exact', label='Number of employees')
	min_number_of_employees = NumberFilter(field_name='number_of_employees', method='filter_number_of_employee_gte', 
								label='Number of employees is great than or equal to')
	max_number_of_employees = NumberFilter(field_name='number_of_employees', method='filter_number_of_employee_lte',
								label='Number of employees is less than or equal to')

	class Meta:
		model = Profession
		fields = (
				'name',
				'number_of_employees',
				'min_number_of_employees',
				'max_number_of_employees',
			)

	def filter_number_of_employee_exact(self, queryset, field_name, value):
		return queryset.annotate(number_of_employees=Count('employees')).filter(number_of_employees=value)

	def filter_number_of_employee_gte(self, queryset, field_name, value):
		return queryset.annotate(number_of_employees=Count('employees')).filter(number_of_employees__gte=value)

	def filter_number_of_employee_lte(self, queryset, field_name, value):
		return queryset.annotate(number_of_employees=Count('employees')).filter(number_of_employees__lte=value)


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
	number_of_employees = NumberFilter(field_name='number_of_employees', method='filter_number_of_employee_exact', label='Number of employees')
	min_number_of_employees = NumberFilter(field_name='number_of_employees', method='filter_number_of_employee_gte', 
								label='Number of employees is great than or equal to')
	max_number_of_employees = NumberFilter(field_name='number_of_employees', method='filter_number_of_employee_lte',
								label='Number of employees is less than or equal to')
	number_of_partners = NumberFilter(field_name='number_of_partners', method='filter_number_of_partner_exact', label='Number of partners')
	min_number_of_partners = NumberFilter(field_name='number_of_partners', method='filter_number_of_partner_gte', 
								label='Number of partners is great than or equal to')
	max_number_of_partners = NumberFilter(field_name='number_of_partners', method='filter_number_of_partner_lte',
								label='Number of partners is less than or equal to')

	class Meta:
		model = Company
		fields = (
			'name',
			'type_of_company',
			'country',
			'number_of_employees',
			'min_number_of_employees',
			'max_number_of_employees',
			'number_of_partners',
			'min_number_of_partners',
			'max_number_of_partners',
			'year_of_foundation',
			'from_year_of_foundation',
			'to_year_of_foundation',
		)

	def filter_number_of_employee_exact(self, queryset, field_name, value):
		return queryset.annotate(number_of_employees=Count('employees')).filter(number_of_employees=value)

	def filter_number_of_employee_gte(self, queryset, field_name, value):
		return queryset.annotate(number_of_employees=Count('employees')).filter(number_of_employees__gte=value)

	def filter_number_of_employee_lte(self, queryset, field_name, value):
		return queryset.annotate(number_of_employees=Count('employees')).filter(number_of_employees__lte=value)

	def filter_number_of_partner_exact(self, queryset, field_name, value):
		return queryset.annotate(number_of_partners=Count('partners')).filter(number_of_partners=value)

	def filter_number_of_partner_gte(self, queryset, field_name, value):
		return queryset.annotate(number_of_partners=Count('partners')).filter(number_of_partners__gte=value)

	def filter_number_of_partner_lte(self, queryset, field_name, value):
		return queryset.annotate(number_of_partners=Count('partners')).filter(number_of_partners__lte=value)


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
