from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta

# Welder
class Welder(TimeStampedModel):
	# id
	first_name = models.CharField(max_length=128, verbose_name='First Name')
	last_name = models.CharField(max_length=128, verbose_name='Last Name')
	welder_stamp = models.ForeignKey('core.WelderStampLov', verbose_name='Welder Stamp')

	class Meta:
		permissions = (
			("select_welderlist", "Can select welder"),
		)

	def __unicode__(self):
		return self.id
	
	def get_absolute_url(self):
		return reverse('welder_detail', kwargs={'pk': self.pk})

# PerformanceQualification
class PerformanceQualification(TimeStampedModel):
	# id
	welder = models.ForeignKey('Welder')
	absa_number = models.CharField(max_length=16, verbose_name='ABSA Number')
	f_number = models.ForeignKey('core.fNumberLov', verbose_name=' f Number')
	process = models.ForeignKey('core.ProcessLov', verbose_name='Process')
	t_qual = models.ForeignKey('core.tQualLov', verbose_name=' t Qual')
	minimum_diameter = models.ForeignKey('core.DiameterLov', verbose_name='Minimum Diameter')
	position = models.ForeignKey('core.PositionLov', verbose_name='Position')
	cessco_weld_procedure = models.ForeignKey('core.CesscoWeldProcedureLov', verbose_name='Cessco Weld Procedure')
	start_date = models.DateField(null=True, blank=True, verbose_name='Original Test Date')
	end_date = models.DateField(null=True, blank=True, verbose_name='End Date')
	active = models.BooleanField()

	def get_absolute_url(self):
		return reverse('performancequalification_detail', kwargs={'pk': self.pk})

	@property
	def renewal_date(self):
		days_in_year=365.2425

		# Get the current date
		today = datetime.now().date()

		# add initial two years to original test date
		continuity_date = self.start_date + timedelta(days=(days_in_year*2))

		if continuity_date < today:
			count = 0
			while (continuity_date < today):
				continuity_date = continuity_date + timedelta(days=(days_in_year/2))

		return continuity_date

# WelderHistory
class WelderHistory(TimeStampedModel):
	# id
	welder = models.ForeignKey('Welder')
	start_date = models.DateField(null=True, blank=True, verbose_name='Start Date')
	end_date = models.DateField(null=True, blank=True, verbose_name='End Date')

	def __unicode__(self):
		return self.id
	
	def get_absolute_url(self):
		return reverse('welderhistory_detail', kwargs={'pk': self.pk})

# WelderStampHistory
