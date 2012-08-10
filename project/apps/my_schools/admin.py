from django.contrib import admin

from my_schools.models import Person, PersonSchool

# class EmailSubscriptionOptions(admin.ModelAdmin):
#     list_display = ('email',)
#     search_fields = ('email',)

admin.site.register(Person)
admin.site.register(PersonSchool)