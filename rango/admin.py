from django.contrib import admin
from rango.models import Category, Page




# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')




admin.site.register(Page, QuestionAdmin)
admin.site.register(Category)
