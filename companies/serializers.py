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

	class Meta:
		model = Profession
		fields = ('name',
				  'description',
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


class CompanySerializer(serializers.ModelSerializer):
	"""
	Serializer for represent list of companies
	"""

	url = serializers.HyperlinkedIdentityField(view_name='companies:company-detail') # url to detail page for company
	year_of_foundation = serializers.DateTimeField(format=DATETIME_FORMAT) # date of foundation with new format

	class Meta:
		model = Company 
		fields = ('name', 'tagline', 'type_of_company', 'year_of_foundation', 'country', 'url')


class PartnerShipSerializer(serializers.ModelSerializer):
	company_inviter = serializers.SlugRelatedField(read_only=True, slug_field='name')
	company = serializers.SlugRelatedField(read_only=True, slug_field='name')

	class Meta:
		model = PartnerShip
		fields = ('company_inviter', 'company',)


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
	partners = serializers.HyperlinkedRelatedField(queryset=Company.objects.all(), many=True, view_name='companies:company-detail') 
	# represent companies that are partners to this company
	year_of_foundation = serializers.DateTimeField(format=DATETIME_FORMAT) # date of foundation with new format
	partnerships = PartnerShipSerializer(many=True, read_only=True)

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
				  'partnerships',
				  'employees',
				  )