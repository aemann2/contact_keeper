from django.contrib import admin
from .models import User, Contact

# Register your models here.
admin.site.register(User)


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    fields = (
        "owner",
        "name",
        "email",
        "phone",
        "contact_type",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "contact_type",
    )


admin.site.register(Contact, ContactAdmin)
