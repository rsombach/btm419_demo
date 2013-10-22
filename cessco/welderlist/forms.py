from django import forms

from models import Welder

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class WelderCreateForm(forms.ModelForm):
	class Meta:
		model = Welder
		first_name = forms.CharField(max_length=128)
		last_name = forms.CharField(max_length=128)
		absa_number = forms.CharField(max_length=16)

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('submit', 'Save Welder'))

