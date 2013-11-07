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

class WelderUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WelderUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Update Welder', css_class='btn-default'))

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

	class Meta:
		model = PerformanceQualification
		
		exclude = [ 'welder' ]
		

class PerformanceQualificationUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PerformanceQualificationUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Update Performance Qualification', css_class='btn-default'))

	class Meta:
		model = PerformanceQualification
		
		exclude = [ 'welder' ]

