from django.contrib import admin

from events.models import Event

# class EmailSubscriptionOptions(admin.ModelAdmin):
#     list_display = ('email',)
#     search_fields = ('email',)

admin.site.register(Event)