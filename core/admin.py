from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address
# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


def make_order_being_deliver(modeladmin, request, queryset):
    queryset.update(ordered=False, being_delivered=True)


def make_order_received(modeladmin, request, queryset):
    queryset.update(being_delivered=False, received=True)


def make_order_refund_requested(modeladmin, request, queryset):
    queryset.update(received=False, refund_requested=True)


make_refund_accepted.short_description = "Update orders to refund granted"
make_order_being_deliver.short_description = "Update orders to being delivered"
make_order_received.short_description = "Update orders to received"
make_order_refund_requested.short_description = "Update orders to refund requested"


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'billing_address',
        'shipping_address',
        'payment',
        'coupon',
    ]
    list_display_links = [
        'user',
        'billing_address',
        'shipping_address',
        'payment',
        'coupon',
    ]
    list_filter = [
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
    ]

    search_fields = [
        'user__username',
        'ref_code',
    ]

    actions = [
        make_order_being_deliver,
        make_order_received,
        make_order_refund_requested,
        make_refund_accepted,
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default',
    ]
    list_filter = [
        'default',
        'address_type',
        'country',
    ]
    search_fields = [
        'user__username',
        'street_address',
        'apartment_address',
        'zip',
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)