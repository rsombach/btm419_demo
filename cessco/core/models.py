from django.db import models
from model_utils.models import TimeStampedModel

# LOV Tables
class fNumberLov(TimeStampedModel):
	# id
	f_number_code = models.CharField(max_length=16)
	f_number_description = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.f_number_code

	class Meta:
		verbose_name = " f Number"
		verbose_name_plural = " f Number "


class ProcessLov(TimeStampedModel):
	# id
	process_code = models.CharField(max_length=16)
	process_description = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.process_code

	class Meta:
		verbose_name = "Process "
		verbose_name_plural = "Process "

class tQualLov(TimeStampedModel):
	# id
	t_qual_code = models.CharField(max_length=16)
	t_qual_description = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.t_qual_code

	class Meta:
		verbose_name = " t Qual "
		verbose_name_plural = " t Qual "

class DiameterLov(TimeStampedModel):
	# id
	diameter_code = models.CharField(max_length=16)
	diameter_description = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.diameter_code

	class Meta:
		verbose_name = "Diameter "
		verbose_name_plural = "Diameter "

class PositionLov(TimeStampedModel):
	# id
	position_code = models.CharField(max_length=16)
	position_description = models.CharField(max_length=256, blank=True)
	
	def __unicode__(self):
		return self.position_code

	class Meta:
		verbose_name = "Position "
		verbose_name_plural = "Position "

class CesscoWeldProcedureLov(TimeStampedModel):
	# id
	cessco_weld_procedure_code = models.CharField(max_length=16)
	cessco_weld_procedure_description = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.cessco_weld_procedure_code

	class Meta:
		verbose_name = "Cessco Weld Procedure "
		verbose_name_plural = "Cessco Weld Procedure "
        
class WelderStampLov(TimeStampedModel):
	# id
	welder_stamp_code = models.CharField(max_length=16)
	welder_stamp_description = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.welder_stamp_code

	class Meta:
		verbose_name = "Welder Stamp "
		verbose_name_plural = "Welder Stamp "