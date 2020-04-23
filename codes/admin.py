from django.contrib import admin
from .models import System, Packages, CodesH6, DriveType


# Register your models here.
@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_time')

    # 保存数据到数据库，本用户只能看本用户下面的内容
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SystemAdmin, self).save_model(request, obj, form, change)


@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_time')

    # 保存数据到数据库，本用户只能看本用户下面的内容
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PackagesAdmin, self).save_model(request, obj, form, change)


@admin.register(DriveType)
class DriveTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_time')

    # 保存数据到数据库，本用户只能看本用户下面的内容
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(DriveTypeAdmin, self).save_model(request, obj, form, change)


@admin.register(CodesH6)
class CodesH6Admin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'owner', 'created_time')

    # 保存数据到数据库，本用户只能看本用户下面的内容
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CodesH6Admin, self).save_model(request, obj, form, change)