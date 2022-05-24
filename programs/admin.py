from django.contrib import admin

from .models import IntelligentProgram, ArtProgram, EducationalProgram

# Register your models here.

admin.site.register(IntelligentProgram)
admin.site.register(ArtProgram)
admin.site.register(EducationalProgram)
