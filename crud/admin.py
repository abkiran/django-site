from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Language)
# admin.site.register(Interest)
@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('interest', 'is_active')
    # list_editable = ('interest', )

admin.site.register(Hotel)
admin.site.register(Neighborhood)