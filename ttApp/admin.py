from django.contrib import admin

from ttApp.models import *


class StoreAdmin(admin.ModelAdmin):
    fields = ('title', 'summary', 'description', 'specs', 'shipping_info', 'price', 'img', 'seller')
    list_display = ('id', 'title', 'seller', 'bought')
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True



# # Register your models here.
admin.site.register(Product, StoreAdmin)
admin.site.register(Favorite)



# Register your models here.
