from django import forms

from crispy_forms.helper import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import *

from .models import Welder
from .models import PerformanceQualification
from .models import WelderHistory
from core.models import WelderStampLov


class WelderCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WelderCreateForm, self).__init__(*args, **kwargs)

		self.fields['welder_stamp'] = forms.ModelChoiceField(queryset=WelderStampLov.objects.exclude(id__in=Welder.objects.values_list('welder_stamp', flat=True)), label=('Welder Stamp'))

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
		self.current_welder_id = kwargs.pop('current_welder_id', None)
		
		super(WelderUpdateForm, self).__init__(*args, **kwargs)

		# Combine the available welder_stamp list with the currently assigned stamp			
		welder_stamp = WelderStampLov.objects.filter(id__in=Welder.objects.values_list('welder_stamp', flat=True).filter(pk=self.current_welder_id))
		assigned_welder_stamp = WelderStampLov.objects.exclude(id__in=Welder.objects.values_list('welder_stamp', flat=True))
		available_welder_stamp_queryset = welder_stamp | assigned_welder_stamp
		
		self.fields['welder_stamp'] = forms.ModelChoiceField(queryset=available_welder_stamp_queryset)

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

class WelderHistoryCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WelderHistoryCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Save Welder History'))

	class Meta:
		model = WelderHistory
		
		exclude = [ 'welder' ]
		
class WelderHistoryUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WelderHistoryUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'

		self.helper.add_input(Submit('submit', 'Update Welder History', css_class='btn-default'))

	class Meta:
		model = WelderHistory
		
		exclude = [ 'welder' ]