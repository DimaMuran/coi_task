from django.contrib import admin
from .models import Direction, Doctor


class DirectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'sort_number',
    )
    list_filter = (
        'name',
        'slug',
        'sort_number',
    )
    search_fields = (
        'name',
        'slug',
        'sort_number',
    )


class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'get_direction',
        'description',
        'birthday',
        'experience',
        'sort_number',
    )
    list_filter = (
        'name',
        'slug',
        'direction',
        'description',
        'birthday',
        'experience',
        'sort_number',
    )
    search_fields = (
        'name',
        'slug',
        'direction__name',
        'description',
        'birthday',
        'experience',
        'sort_number',
    )

    def get_direction(self, obj):
        return '\n'.join(p.name for p in obj.direction.all())


admin.site.register(Direction, DirectionAdmin)
admin.site.register(Doctor, DoctorAdmin)
