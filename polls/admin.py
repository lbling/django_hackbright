from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.


#adds polls choices in-line
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('question', 'pub_date', 'was_published_recently')
	
	fieldsets =[
		(None,	{'fields' : ['question']}),
		('Date Information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
		]
	inlines = [ChoiceInLine]
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)




