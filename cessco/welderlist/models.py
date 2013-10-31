from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel

# Welder
class Welder(TimeStampedModel):
	# id
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	absa_number = models.CharField(max_length=16)

	def __unicode__(self):
		return self.id

	def get_absolute_url(self):
		return reverse('welder_detail', kwargs={'pk': self.pk})

# WelderStamp
class WelderStamp(TimeStampedModel):
	# id
	stamp = models.CharField(max_length=4)

# PerformanceQualification
class PerformanceQualification(TimeStampedModel):
	# id
	welder = models.ForeignKey('Welder')
	pq_card_number = models.IntegerField()
	f_number = models.ForeignKey('core.fNumberLov')
	process = models.ForeignKey('core.ProcessLov')
	t_qual = models.ForeignKey('core.tQualLov')
	minimum_diameter = models.ForeignKey('core.DiameterLov')
	position = models.ForeignKey('core.PositionLov')
	cessco_weld_procedure = models.ForeignKey('core.CesscoWeldProcedureLov')
	original_test_date = models.DateField(null=True, blank=True)
	renewal_date = models.DateField(null=True, blank=True)
	active = models.BooleanField()

	def get_absolute_url(self):
		return reverse('performancequalification_detail', kwargs={'pk': self.pk})

	# def save(self, *args, **kwargs):
	# 	# Call the "real" save() method.
	# 	super(PerformanceQualification, self).save(*args, **kwargs)

# WelderStampHistory
