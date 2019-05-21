from django.db import models

# Create your models here.
class Project(models.Model):
	titulo=models.CharField(max_length=30,verbose_name='Titulo del Proyecto')
	descripcion=models.TextField()
	imagen=models.ImageField(upload_to='proyectos')
	link=models.URLField(null=True,blank=True,verbose_name='URL del proyecto')
	create=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creación')
	update=models.DateTimeField(auto_now=True,verbose_name='Fecha de Actualización')

	class Meta:
		verbose_name='Proyecto'
		verbose_name_plural='Mis Proyectos'

	def __str__(self):
		return self.titulo

