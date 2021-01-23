from django.contrib import admin

from order.models import ShopCart, Order, OrderProduct


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'size', 'color', 'get_final_price']
    list_filter = ['user']

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'price', 'quantity', 'status')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'region', 'district', 'street_address', 'apartment_address', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'region', 'district', 'street_address', 'apartment_address', 'phone', 'first_name', 'ip', 'last_name', 'total')
    can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'status']
    list_filter = ['status', 'user']


# Register your models here.
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
