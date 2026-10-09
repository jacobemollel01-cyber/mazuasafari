
from django.contrib import admin
from .models import SafariInquiry, ContactMessage


@admin.register(SafariInquiry)
class SafariInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "destination",
        "travellers",
        "arrival",
        "created_at",
    )

    list_filter = (
        "destination",
        "accommodation",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "country",
    )

    ordering = ("-created_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "destination",
        "created_at",
    )

    list_filter = (
        "destination",
        "accommodation",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "country",
        "requests",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at",)