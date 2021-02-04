from django.contrib import admin

from consent_user_information.models import ConsentUserInformation


class ConsentUserInformationAdmin(admin.ModelAdmin):
    """Admin for consent user information"""

    list_display = ("user", "ip", "device", "browser", "user_agent", "created_at")
    raw_id_fields = ("user",)
    readonly_fields = (
        "user",
        "ip",
        "device",
        "browser",
        "user_agent",
        "os",
        "created_at",
    )
    search_fields = ["user__email", "user__first_name", "user__last_name"]


admin.site.register(ConsentUserInformation, ConsentUserInformationAdmin)
