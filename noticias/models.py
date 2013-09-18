from django.db import models

class Noticia(models.Model):
	titulo = models.CharField( max_length=500 )
	fecha = models.DateField()
	extracto = models.TextField()
	descripcion = models.TextField()
	fuente = models.CharField( max_length=800, blank=True, null=True )
	imagen = models.ImageField( upload_to="uploads/%Y/%m/%d", blank=True, null=True, default="uplaods/noimage.png" )

	created_at = models.DateTimeField( auto_now_add=True, blank=True, null=True )
	modified_at = models.DateTimeField( auto_now=True, blank=True, null=True )


	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name = "noticia"
		verbose_name_plural = "noticias"
		get_latest_by = "created_at"
