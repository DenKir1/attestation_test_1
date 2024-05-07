from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronics.models import Product, Contact, Seller


admin.site.register(Product)
admin.site.register(Contact)


@admin.action(description="Списание задолженности")
def debt_nulled(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):

    def supplier_link(self, obj):
        link = reverse("admin:electronics_seller_change", args=[obj.supplier.id])
        linkify = format_html('<a href="{}">{}</a>', link, obj.supplier.name) if obj else None
        return linkify

    supplier_link.allow_tags = True
    supplier_link.short_description = 'ПОСТАВЩИК'
    list_display = ('name', 'seller_type', 'contact', 'supplier_link', 'debt', 'created', )

    list_filter = ('seller_type', 'contact__city',)
    actions = [debt_nulled, ]
