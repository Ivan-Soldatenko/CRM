from rest_framework import serializers 
from companies.models import Profession, Company, Employee, PartnerShip
from crm.settings import DATETIME_FORMAT


class ProfessionSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent list of professions
	"""

	url = serializers.HyperlinkedIdentityField(view_name='companies:profession-detail') # url to detail page for profession

	class Meta:
		model = Profession 
		fields = ('name', 'url')


class ProfessionEmployeeSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent employee model in profession model
	"""

	url = serializers.HyperlinkedIdentityField(view_name='companies:employee-detail') # url to detail page for employee
	company = serializers.SlugRelatedField(read_only=True, slug_field='name') # name of related company to this employee

	class Meta:
		model = Employee 
		fields = ('name', 'company', 'url')


class DetailProfessionSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent detail information of profession
	"""

	employees = ProfessionEmployeeSerializer(many=True, read_only=True) # represent all employees related to this profession
	number_of_employees = serializers.IntegerField(source='count_employees', read_only=True) 
	# number of employees that are belong to this profession

	class Meta:
		model = Profession
		fields = ('name',
				  'description',
				  'number_of_employees',
				  'employees')


class EmployeeSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent list of employees
	"""

	url = serializers.HyperlinkedIdentityField(view_name='companies:employee-detail') # url to detail page for employee
	profession = serializers.SlugRelatedField(read_only=True, slug_field='name') # name of related profession to this employee
	company = serializers.SlugRelatedField(read_only=True, slug_field='name') # name of related company to this employee

	class Meta:
		model = Employee
		fields = ('name', 'profession', 'company', 'url')


class DetailEmployeeSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent detail information of employee
	"""

	profession = serializers.HyperlinkedRelatedField(queryset=Profession.objects.all(), view_name='companies:profession-detail') # name of related profession to this employee
	company = serializers.HyperlinkedRelatedField(queryset=Company.objects.all(), view_name='companies:company-detail') # name of related company to this employee
	hired_date = serializers.DateTimeField(format=DATETIME_FORMAT) # hired date with new format
	promotion_date = serializers.DateTimeField(format=DATETIME_FORMAT) # promotion date with new format

	class Meta:
		model = Employee
		fields = ('name', 
				 'age', 
				 'gender', 
				 'photo', 
				 'hired_date', 
				 'company', 
				 'profession', 
				 'salary', 
				 'promotion_date', 
				 'phone_number', 
				 'email')


class PartnerShipSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent list of partnerships
	"""

	info = serializers.CharField(source='__str__', read_only=True) # short information about companies that have a partnership
	url = serializers.HyperlinkedIdentityField(view_name='companies:partnership-detail') # url to detail page for partnership

	class Meta:
		model = PartnerShip
		fields = ('info', 'url',)


class DetailPartnerShipSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent detail information of partnerships
	"""

	info = serializers.CharField(source='__str__', read_only=True) # short information about companies that have a partnership
	company = serializers.HyperlinkedRelatedField(view_name='companies:company-detail', read_only=True)
	# name of company, which is partner to company_inviter
	company_inviter = serializers.HyperlinkedRelatedField(view_name='companies:company-detail', read_only=True)
	# name of company, which starts partnerships with company

	class Meta:
		model = PartnerShip
		fields = ('info', 'company', 'company_inviter', 'joint_products', 'year_partnership')


class CompanySerializer(serializers.ModelSerializer):
	"""
	Serializer for represent list of companies
	"""

	url = serializers.HyperlinkedIdentityField(view_name='companies:company-detail') # url to detail page for company
	year_of_foundation = serializers.DateTimeField(format=DATETIME_FORMAT) # date of foundation with new format
	number_of_employees = serializers.IntegerField(source='count_employees') # number of employees that are belong to this company
	number_of_partners = serializers.IntegerField(source='count_partners') # number of company that have partnership with this company

	class Meta:
		model = Company 
		fields = ('name', 
				'tagline', 
				'type_of_company', 
				'year_of_foundation', 
				'country', 
				'number_of_employees',
				'number_of_partners',
				'url')


class CompanyEmployeeSerializer(serializers.ModelSerializer):
	"""
	Serializer for represent employee model in company model
	"""

	url = serializers.HyperlinkedIdentityField(view_name='companies:employee-detail') # url to detail page for employee
	profession = serializers.SlugRelatedField(read_only=True, slug_field='name') # name of related profession to this employee

	class Meta:
		model = Employee
		fields = ('name', 'profession', 'url')


class DetailCompanySerializer(serializers.ModelSerializer):
	"""
	Serializer for represent detail information of company
	"""

	employees = CompanyEmployeeSerializer(many=True, read_only=True) # represent all employees related to this company
	partners = serializers.HyperlinkedRelatedField(queryset=Company.objects.all(), many=True, view_name='companies:company-detail', write_only=True) 
	# represent companies that are partners to this company
	year_of_foundation = serializers.DateTimeField(format=DATETIME_FORMAT) # date of foundation with new format
	partnerships = PartnerShipSerializer(many=True, read_only=True)
	number_of_employees = serializers.IntegerField(source='count_employees', read_only=True) # number of employees that are belong to this company
	number_of_partners = serializers.IntegerField(source='count_partners', read_only=True) # number of company that have partnership with this company

	class Meta:
		model = Company 
		fields = ('name',
				  'logo',
				  'tagline',
				  'type_of_company',
				  'description',
				  'year_of_foundation',
				  'country',
				  'phone_number',
				  'email',
				  'partners',
				  'number_of_employees',
				  'number_of_partners',
				  'partnerships',
				  'employees',
				  )