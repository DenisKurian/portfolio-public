from django.contrib import admin
from .models import Project, Certificates, Skills, Resume, ProjectImage

admin.site.register(Project)
admin.site.register(Certificates)
admin.site.register(Skills)
admin.site.register(Resume)
admin.site.register(ProjectImage)

