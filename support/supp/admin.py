from django.contrib import admin

from .models import Cars, CarsInUse, Employees, Entities, Tasks, Customers


class TasksInline(admin.TabularInline):
    model = Tasks


@admin.register(Entities)
class EntitiesAdmin(admin.ModelAdmin):
    search_fields = ("name__icontains",)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    inlines = [
        TasksInline,
    ]


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    fields = (
        "phone",
        "title",
        "description",
        "status",
        "priority",
        "entity",
        "slave",
        "act",
        "summary",
        "agreement",
    )
    list_display = ("title", "entity", "slave", "created", "status")
    search_fields = (
        "title",
        "created",
        "creator",
        "entity__name",
        "status",
        "priority",
        "slave__username",
        "act",
        "agreement",
    )
    list_filter = (
        "created",
        "status",
        "priority",
        "entity",
        "slave",
        "act",
        "agreement",
    )


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    search_fields = ("model", "state_number")


@admin.register(CarsInUse)
class CarsInUseAdmin(admin.ModelAdmin):
    pass


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    search_fields = ("name", "object", "phone")
