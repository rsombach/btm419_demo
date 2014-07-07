from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel

# Unit
class Unit(TimeStampedModel):
	# id
	business_unit = models.ForeignKey('core.BusinessUnitLov', verbose_name='Business Unit')
	unit_type = models.ForeignKey('core.UnitTypeLov', verbose_name='Unit Type')
	unit_make = models.ForeignKey('core.UnitMakeLov', verbose_name='Unit Make')
	model = models.CharField(max_length=256)
	serial_number =models.CharField(max_length=32)
	start_date = models.DateField(null=True, blank=True, verbose_name='Inservice Date')
	active = models.BooleanField()

	class Meta:
		permissions = (
			("select_calibration", "Can select unit"),
		)

	def __unicode__(self):
		return self.id

	def get_absolute_url(self):
		return reverse('unit_detail', kwargs={'pk': self.pk})

# UnitHistory
class UnitHistory(TimeStampedModel):
	# id
	unit = models.ForeignKey('calibration.Unit', verbose_name='Unit')
	calibrated_by = models.CharField(max_length=256)
	comment = models.CharField(max_length=256)
	certificate_issued = models.BooleanField()
	calibration_date_time = models.DateField(null=True, blank=True, verbose_name='Callibration Date')

	def __unicode__(self):
		return self.id