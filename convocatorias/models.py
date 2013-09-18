from django.db import models

class Convocatoria(models.Model):
	titulo = models.CharField( max_length=500 )
	fecha = models.DateField()
	extracto = models.TextField()
	descripcion = models.TextField()
	imagen = models.ImageField( upload_to="uploads/%Y/%m/%d", blank=True, null=True, default="uplaods/noimage.png" )

	created_at = models.DateTimeField( auto_now_add=True, blank=True, null=True )
	modified_at = models.DateTimeField( auto_now=True, blank=True, null=True )

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name = "convocatoria"
		verbose_name_plural = "convocatorias"

