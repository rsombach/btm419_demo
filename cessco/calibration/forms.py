from django import forms

from crispy_forms.helper import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import *

from .models import Unit
from core.models import BusinessUnitLov


class UnitCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UnitCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Unit'))

	class Meta:
		model = Unit


class UnitUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		# self.current_welder_id = kwargs.pop('current_welder_id', None)
		
		super(UnitUpdateForm, self).__init__(*args, **kwargs)


		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Update Unit', css_class='btn-default'))

	class Meta:
		model = Unit