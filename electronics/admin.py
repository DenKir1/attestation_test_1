from django.contrib import admin
from electronics.models import Product, Contact, Seller


admin.site.register(Product)
admin.site.register(Contact)


@admin.action(description="Списание задолженности")
def debt_nulled(modeladmin, request, queryset):
    queryset.update(debt=0)

# def linkify(field_name):
#     def _linkify(obj):
#         linked_obj = getattr(obj, field_name)
#         if linked_obj is None:
#             return '-'
#         app_label = linked_obj._meta.app_label
#         model_name = linked_obj._meta.model_name
#         view_name = f'admin:{app_label}_{model_name}_change'
#         link_url = reverse(view_name, args=[linked_obj.pk])
#         return format_html('<a href="{}">{}</a>', link_url, linked_obj)
#     _linkify.short_description = field_name
#     return _linkify


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller_type', 'supplier',)
    list_display_links = ('name', linkify(field_name='supplier'),)
    list_filter = ('seller_type', 'contact__city',)
    actions = [debt_nulled, ]

    # def contact_city(self, obj):
    #     return obj.contacts.city
    # def link_to_bar(self, obj):
    #     link = urlresolvers.reverse('admin:app_bar_change', args=[obj.bar_id])
    #     return format_html('<a href="{}">{}</a>', link, obj.bar) if obj.bar else None