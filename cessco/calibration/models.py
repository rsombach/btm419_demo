from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta

import re

# Unit
class Unit(TimeStampedModel):
	# id
	business_unit = models.ForeignKey('core.BusinessUnitLov', verbose_name='Business Unit')
	unit_type = models.ForeignKey('core.UnitTypeLov', verbose_name='Unit Type')
	unit_make = models.ForeignKey('core.UnitMakeLov', verbose_name='Unit Make')
	model = models.CharField(null=True, blank=True, max_length=256)
	serial_number =models.CharField(null=True, blank=True, max_length=32, verbose_name='Serial Number')
	start_date = models.DateField(null=True, blank=True, verbose_name='Inservice Date')
	active = models.BooleanField()
	renewal_period = models.ForeignKey('core.UnitRenewalPeriodLov', verbose_name='Renewal Period')

	class Meta:
		permissions = (
			("select_calibration", "Can select unit"),
		)

	def __unicode__(self):
		return self.id

	def get_absolute_url(self):
		return reverse('unit_detail', kwargs={'pk': self.pk})

	@property
	def calibration_due_date(self):
		# define the length of a month based on a year (this is "good enough")
		days_in_a_month = (365.2425 / 12)

		unithistory_qs = []
		unithistory_qs = UnitHistory.objects.filter(unit_id=self.id, calibrated=True).order_by('-service_date_time')

		# return the lastest service date that is a calibration and add the renwal period to the date
		if unithistory_qs.count() > 0:
			last_service_date = unithistory_qs[0].service_date_time
			s = str(self.renewal_period)
			renewal_period = map(int, re.findall('\d+', s))

			return last_service_date + timedelta(days=(renewal_period[0] * days_in_a_month))
		else:
		    return None

# UnitHistory
class UnitHistory(TimeStampedModel):
	# id
	unit = models.ForeignKey('calibration.Unit', verbose_name='Unit')
	calibrated_by = models.CharField(max_length=256, verbose_name='Serviced By')
	comment = models.CharField(null=True, blank=True, max_length=2048)
	certificate_issued = models.BooleanField(verbose_name='Certificate Issued')
	service_date_time = models.DateField(verbose_name='Service Date')
	calibrated = models.BooleanField(verbose_name='Calibrated')

	def __unicode__(self):
		return self.id

	def get_absolute_url(self):
		return reverse('unithistory_detail', kwargs={'pk': self.pk})