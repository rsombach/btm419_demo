from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel

# Welder
class Welder(TimeStampedModel):
	# id
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	welder_stamp = models.ForeignKey('core.WelderStampLov')

	def __unicode__(self):
		return self.id
	
	def get_absolute_url(self):
		return reverse('welder_detail', kwargs={'pk': self.pk})

# PerformanceQualification
class PerformanceQualification(TimeStampedModel):
	# id
	welder = models.ForeignKey('Welder')
	absa_number = models.CharField(max_length=16)
	f_number = models.ForeignKey('core.fNumberLov')
	process = models.ForeignKey('core.ProcessLov')
	t_qual = models.ForeignKey('core.tQualLov')
	minimum_diameter = models.ForeignKey('core.DiameterLov')
	position = models.ForeignKey('core.PositionLov')
	cessco_weld_procedure = models.ForeignKey('core.CesscoWeldProcedureLov')
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	active = models.BooleanField()

	def get_absolute_url(self):
		return reverse('performancequalification_detail', kwargs={'pk': self.pk})

# WelderStampHistory
