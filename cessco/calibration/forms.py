from django import forms

from crispy_forms.helper import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import *

from .models import Unit
from .models import UnitHistory

from core.models import BusinessUnitLov, UnitMakeLov


class UnitCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UnitCreateForm, self).__init__(*args, **kwargs)

		self.fields['unit_make'] = forms.ModelChoiceField(queryset=UnitMakeLov.objects.order_by('unit_make_code'), label=('Unit Make'))

		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Unit'))

	class Meta:
		model = Unit
		fields = ['business_unit', 'unit_type', 'unit_make', 'model', 'serial_number', 'start_date', 'renewal_period', 'comment', 'active']


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
		fields = ['business_unit', 'unit_type', 'unit_make', 'model', 'serial_number', 'start_date', 'renewal_period', 'comment', 'active']

class UnitHistoryCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UnitHistoryCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Unit History'))

	class Meta:
		model = UnitHistory

		exclude = [ 'unit' ]
		fields = ['service_date_time', 'calibrated_by', 'comment', 'certificate_issued', 'calibrated' ]

class UnitHistoryUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		# self.current_welder_id = kwargs.pop('current_welder_id', None)
		
		super(UnitHistoryUpdateForm, self).__init__(*args, **kwargs)


		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Update Unit History', css_class='btn-default'))

	class Meta:
		model = UnitHistory

		exclude = [ 'unit' ]