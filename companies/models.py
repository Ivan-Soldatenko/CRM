from django.db import models


class Profession(models.Model):
	"""
	Model for representing profession
	"""

	name = models.CharField(max_length=50, blank=False, unique=True)
	description = models.TextField(blank=False)

	class Meta:
		ordering = ('name',)
	
	def __str__(self):
		return self.name


class Company(models.Model):
	"""
	Model for representing company
	"""

	name = models.CharField(max_length=100, blank=False, unique=True)
	logo = models.ImageField(upload_to='companies/logos')
	tagline = models.CharField(max_length=100)
	type_of_company = models.CharField(max_length=100, blank=False)
	description = models.TextField()
	year_of_foundation = models.DateTimeField(blank=False)
	country = models.CharField(max_length=100, blank=False)
	phone_number = models.CharField(max_length=13)
	email = models.EmailField(max_length=100)
	partners = models.ManyToManyField('self', blank=True, through='PartnerShip') # 'self' = Company in this case, because partners are others companies

	class Meta:
		ordering = ('name', )

	def __str__(self):
		return self.name 


class PartnerShip(models.Model):
	"""
	Model for representing relationship between partners
	"""

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	company_inviter = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='partnerships')
	joint_products = models.CharField(max_length=250, blank=True, default='')
	year_partnership = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-year_partnership', )
		unique_together = ('company', 'company_inviter')

	def __str__(self):
		return f"Partnership between {self.company_inviter.name} and {self.company.name}"


class Employee(models.Model):
	"""
	Model for representing employee
	"""

	# For choice in gender's attribute
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = ( 
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)

	name = models.CharField(max_length=100, blank=False, unique=True)
	age = models.PositiveSmallIntegerField(blank=False)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE, blank=False)
	photo = models.ImageField(upload_to='employees/photos')
	hired_date = models.DateTimeField(auto_now_add=True)
	company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
	profession = models.ForeignKey(Profession, related_name='employees', on_delete=models.CASCADE)
	salary = models.PositiveIntegerField(blank=False)
	promotion_date = models.DateTimeField()
	phone_number = models.CharField(max_length=13)
	email = models.EmailField(max_length=100)

	class Meta:
		ordering = ('profession__name', 'company__name', 'name', )

	def __str__(self):
		return self.name