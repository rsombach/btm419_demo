from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class WelderCreateForm(forms.Form):
	first_name = forms.CharField(max_length=128)
	last_name = forms.CharField(max_length=128)
	absa_number = forms.CharField(max_length=16)


	def __init__(self, *args, **kwargs):
		super(WelderCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-welder-create'
		self.helper.form_class = "form-horizontal"
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Submit'))
