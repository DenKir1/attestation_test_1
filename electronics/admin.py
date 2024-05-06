from django.contrib import admin
from electronics.models import Product, Contact, Seller


admin.site.register(Product)
admin.site.register(Contact)


@admin.action(description="Списание задолженности")
def debt_nulled(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    def link_to_suplier(self, obj):
        link = urlresolvers.reverse('admin:app_bar_change', args=[obj.suplier.id])
        linkify = format_html('<a href="{}">{}</a>', link, obj.suplier.id) if obj.suplier.id else None
        linkify.short_description = obj.suplier.name
        return linkify
        
    list_display = ('name', 'seller_type', 'link_to_suplier',)

    list_filter = ('seller_type', 'contact__city',)
    actions = [debt_nulled, ]
