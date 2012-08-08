from django.contrib import admin

from schools.models import SchoolType, School

# class EmailSubscriptionOptions(admin.ModelAdmin):
#     list_display = ('email',)
#     search_fields = ('email',)

admin.site.register(SchoolType)
admin.site.register(School)