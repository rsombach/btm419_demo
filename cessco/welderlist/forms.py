from django import forms

from crispy_forms.helper import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import *

from .models import Welder
from .models import PerformanceQualification


class WelderCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WelderCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Welder'))

	class Meta:
		model = Welder


class PerformanceQualificationCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PerformanceQualificationCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Performance Qualification', css_class='btn-default'))

		# self.helper.layout = Layout (
		# 	Fieldset (
		# 		Field('welder'),
		# 		Field('pq_card_number'),
		# 		Field('f_number'),
		# 		Field('process'),
		# 		Field('t_qual'),
		# 		Field('minimum_diameter'),
		# 		Field('cessco_weld_procedure'),
		# 		Field('original_test_date'),
		# 		Field('renewal_date'),
		# 		Field('active'),
		# 	),
		# 	FormActions (
		# 	    Submit('submit', 'Save Performance Qualification', css_class='btn-default'),
		# 	)
		# )

	class Meta:
		model = PerformanceQualification
		
		# fields = [
		# 		'welder',
		# 		'pq_card_number',
		# 		'f_number',
		# 		'process',
		# 		't_qual',
		# 		'minimum_diameter',
		# 		'cessco_weld_procedure',
		# 		'original_test_date',
		# 		'renewal_date',
		# 		'active'
		# ]

