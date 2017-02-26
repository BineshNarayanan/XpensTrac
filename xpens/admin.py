from django.contrib import admin

# Register your models here.

from .models import Category, Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'date', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'amount','category__name')
    list_per_page = 25

#admin.site.register(Page, PageAdmin)

admin.site.register(Category)
admin.site.register(Expense,ExpenseAdmin)
