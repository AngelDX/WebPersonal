from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
	readonly_fields=('create','update')
	list_display=('titulo','imagen','create','update')
	ordering=('titulo','create')
	search_fields=('titulo','descripcion')
	date_hierarchy='create'
	list_filter=('titulo','create')

admin.site.register(Project,ProjectAdmin)