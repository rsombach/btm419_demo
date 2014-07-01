from django import forms

from crispy_forms.helper import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import *

from .models import Unit
from core.models import BusinessUnitLov


class UnitCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UnitCreateForm, self).__init__(*args, **kwargs)

		# self.fields['business_unit'] = forms.ModelChoiceField(queryset=BusinessUnitLov.objects.values_list('business_unit_code', flat=True))

		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Unit'))

	class Meta:
		model = Unit