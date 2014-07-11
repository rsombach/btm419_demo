from django.db import models
from model_utils.models import TimeStampedModel

# Core LOV
class BusinessUnitLov(TimeStampedModel):
	# id
	business_unit_code = models.CharField(verbose_name="Business Unit Code", max_length=32, unique=True)
	business_unit_description = models.CharField(verbose_name="Business Unit Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.business_unit_code

	class Meta:
		verbose_name = "Business Unit "
		verbose_name_plural = "Business Unit "


# Welderlist LOV Tables
class fNumberLov(TimeStampedModel):
	# id
	f_number_code = models.CharField(verbose_name=" f Number Code", max_length=32, unique=True)
	f_number_description = models.CharField(verbose_name=" f Number Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.f_number_code

	class Meta:
		verbose_name = " f Number"
		verbose_name_plural = " f Number "


class ProcessLov(TimeStampedModel):
	# id
	process_code = models.CharField(verbose_name="Process Code", max_length=32, unique=True)
	process_description = models.CharField(verbose_name="Process Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.process_code

	class Meta:
		verbose_name = "Process "
		verbose_name_plural = "Process "

class tQualLov(TimeStampedModel):
	# id
	t_qual_code = models.CharField(verbose_name=" t Qual Code", max_length=32, unique=True)
	t_qual_description = models.CharField(verbose_name=" t Qual Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.t_qual_code

	class Meta:
		verbose_name = " t Qual "
		verbose_name_plural = " t Qual "

class DiameterLov(TimeStampedModel):
	# id
	diameter_code = models.CharField(verbose_name="Diameter Code", max_length=32, unique=True)
	diameter_description = models.CharField(verbose_name="Diameter Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.diameter_code

	class Meta:
		verbose_name = "Diameter "
		verbose_name_plural = "Diameter "

class PositionLov(TimeStampedModel):
	# id
	position_code = models.CharField(verbose_name="Position Code", max_length=32, unique=True)
	position_description = models.CharField(verbose_name="Position Description", max_length=256, blank=True)
	
	def __unicode__(self):
		return self.position_code

	class Meta:
		verbose_name = "Position "
		verbose_name_plural = "Position "

class CesscoWeldProcedureLov(TimeStampedModel):
	# id
	cessco_weld_procedure_code = models.CharField(verbose_name="Cessco Weld Procedure Code", max_length=32, unique=True)
	cessco_weld_procedure_description = models.CharField(verbose_name="Cessco Weld Procedure Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.cessco_weld_procedure_code

	class Meta:
		verbose_name = "Cessco Weld Procedure "
		verbose_name_plural = "Cessco Weld Procedure "
        
class WelderStampLov(TimeStampedModel):
	# id
	welder_stamp_code = models.CharField(verbose_name="Welder Stamp Code", max_length=32, unique=True)
	welder_stamp_description = models.CharField(verbose_name="Welder Stamp Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.welder_stamp_code

	class Meta:
		verbose_name = "Welder Stamp "
		verbose_name_plural = "Welder Stamp "


# Calibration LOV Tables
class UnitMakeLov(TimeStampedModel):
	# id
	unit_make_code = models.CharField(verbose_name="Unit Make Code", max_length=32, unique=True)
	unit_make_description = models.CharField(verbose_name="Unit Make Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.unit_make_code

	class Meta:
		verbose_name = "Unit Make "
		verbose_name_plural = "Unit Make "

class UnitTypeLov(TimeStampedModel):
	# id
	unit_type_code = models.CharField(verbose_name="Unit Type Code", max_length=32, unique=True)
	unit_type_description = models.CharField(verbose_name="Unit Type Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.unit_type_code

	class Meta:
		verbose_name = "Unit Type "
		verbose_name_plural = "Unit Type "

class UnitRenewalPeriodLov(TimeStampedModel):
	# id
	unit_renewal_period_code = models.CharField(verbose_name="Unit Renewal Period Code", max_length=32, unique=True)
	unit_renewal_period_description = models.CharField(verbose_name="Unit Renewal Period Description", max_length=256, blank=True)

	def __unicode__(self):
		return self.unit_renewal_period_code

	class Meta:
		verbose_name = "Unit Renewal Period "
		verbose_name_plural = "Unit Renewal Period "


