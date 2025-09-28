from django.contrib import admin
from .models import Project, Tech, TechCategory
from imagekit.admin import AdminThumbnail

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'order')
    admin_thumbnail = AdminThumbnail(image_field='image')

class TechAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'visible', 'order')
    admin_thumbnail = AdminThumbnail(image_field='logo')

class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible', 'order')

admin.site.register(Project, ProjectsAdmin)
admin.site.register(Tech, TechAdmin)
admin.site.register(TechCategory, TechCategoryAdmin)