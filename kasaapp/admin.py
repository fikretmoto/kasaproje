from django.contrib import admin

# Register your models here.

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['tarih', 'aciklama', 'tutar', 'islem_turu']
    list_filter = ['tarih', 'islem_turu']
    search_fields = ['aciklama']
