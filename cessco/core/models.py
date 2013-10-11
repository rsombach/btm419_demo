from django.db import models
from model_utils.models import TimeStampedModel

# LovTables
class fNumberLov(TimeStampedModel):
	# id
	f_number_code = models.CharField(max_length=16)
	f_number_description = models.CharField(max_length=256)
	class Meta:
		verbose_name = " f Number LOV"
		verbose_name_plural = " f Number LOV"

class ProcessLov(TimeStampedModel):
	# id
	process_code = models.CharField(max_length=16)
	process_description = models.CharField(max_length=256)
	class Meta:
		verbose_name = "Process LOV"
		verbose_name_plural = "Process LOV"

class tQualLov(TimeStampedModel):
	# id
	t_qual_code = models.CharField(max_length=16)
	t_qual_description = models.CharField(max_length=256)
	class Meta:
		verbose_name = " t Qual LOV"
		verbose_name_plural = " t Qual LOV"

class DiameterLov(TimeStampedModel):
	# id
	diameter_code = models.CharField(max_length=16)
	diameter_description = models.CharField(max_length=256)
	class Meta:
		verbose_name = "Diameter LOV"
		verbose_name_plural = "Diameter LOV"

class PositionLov(TimeStampedModel):
	# id
	position_code = models.CharField(max_length=16)
	position_description = models.CharField(max_length=256)
	class Meta:
		verbose_name = "Position LOV"
		verbose_name_plural = "Position LOV"

class CesscoWeldProcedureLov(TimeStampedModel):
	# id
	cessco_weld_procedure_code = models.CharField(max_length=16)
	cessco_weld_procedure_description = models.CharField(max_length=256)
	class Meta:
		verbose_name = "Cessco Weld Procedure LOV"
		verbose_name_plural = "Cessco Weld Procedure LOV"