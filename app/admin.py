from django.contrib import admin
from django.contrib.auth.models import User
from .models import Supplier, Item, Contract


@admin.register(Supplier)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'organization_name', 'location', 'phone_number', 'email', 'supplier_rate')
    search_fields = ('organization_name', 'location', 'phone_number', 'email')
    ordering = ('organization_name', 'supplier_rate')


@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'price')
    search_fields = ('item_name',)
    ordering = ('price',)


@admin.register(Contract)
class ContractsAdmin(admin.ModelAdmin):
    list_display = ('contract_id', 'upload_date', 'signed', 'user')
    list_filter = ('signed', 'supplier', 'user')
    search_fields = ('supplier__organization_name', 'user__username')
    readonly_fields = ('contract_id',)
    ordering = ('user__username',)

    def get_document_file_link(self, obj):
        if obj.document_file_path:
            return '<a href="{0}">{1}</a>'.format(obj.document_file_path.url, obj.document_file_path.name)
        else:
            return "Файл не выбран"
    get_document_file_link.allow_tags = True
    get_document_file_link.short_description = 'Документ'


