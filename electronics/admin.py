from django.contrib import admin
from electronics.models import Product, Contact, Seller


admin.site.register(Product)
admin.site.register(Contact)


@admin.action(description="Списание задолженности")
def debt_nulled(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller_type', 'supplier',)
    list_display_links = ('name', 'supplier',)
    list_filter = ('seller_type', 'contact__city',)
    actions = [debt_nulled, ]

    # def contact_city(self, obj):
    #     return obj.contacts.city
