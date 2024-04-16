from django.contrib import admin

from .models import Supplier, Item, Contract, Directorer, Deliver, Finance


@admin.register(Supplier)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name', 'location', 'phone_number', 'email', 'supplier_rate')
    search_fields = ('organization_name', 'location', 'phone_number', 'email')
    ordering = ('organization_name', 'supplier_rate')
    readonly_fields = ("display_items",)

    def display_items(self, obj):
        return (", ".join([item.item_name for item in obj.items.all()])
                + "\n\n\n\nFor more information about classifiers go and check directory.")

    display_items.short_description = 'Items'


@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'formatted_price',)
    search_fields = ('item_name',)
    ordering = ('price',)
    readonly_fields = ("display_suppliers",)

    def formatted_price(self, obj):
        price = str(obj.price)
        currency, amount = price[:3], price[3:]
        return f"{currency} {amount}"

    formatted_price.short_description = "Price"

    def display_suppliers(self, obj):
        return (", ".join([supplier.organization_name for supplier in obj.supplier_set.all()])
                + "\n\n\n\nFor more information about classifiers go and check directory.")

    display_suppliers.short_description = 'Suppliers'


@admin.register(Contract)
class ContractsAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_date', 'signed', 'user')
    list_filter = ('signed', 'supplier', 'user')
    search_fields = ('supplier__organization_name', 'user__username')
    readonly_fields = ('id',)
    ordering = ('user__username',)

    def get_document_file_link(self, obj):
        if obj.document_file_path:
            return '<a href="{0}">{1}</a>'.format(obj.document_file_path.url, obj.document_file_path.name)
        else:
            return "Файл не выбран"
    get_document_file_link.allow_tags = True
    get_document_file_link.short_description = 'Документ'


@admin.register(Directorer)
class DirectoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'data',)
    search_fields = ('name', 'description', 'data',)
    ordering = ('name', 'data', 'description')


@admin.register(Deliver)
class DeliveriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'start_date', 'end_date', 'contract')
    search_fields = ('supplier', 'start_date', 'end_date', 'contract')
    ordering = ('supplier', 'start_date', 'end_date', 'contract')


@admin.register(Finance)
class FinancesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file',)
    search_fields = ('file',)
    ordering = ('file',)
