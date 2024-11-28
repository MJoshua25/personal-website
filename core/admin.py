# vim: set fileencoding=utf-8 :
from django.contrib import admin

import core.models as models


class PersonalInfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_upd',
        'first_name',
        'last_name',
        'birth_date',
        'resume',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'birth_date',
        'id',
        'first_name',
        'last_name',
        'resume',
    )
    raw_id_fields = ('skills',)


class PersonalSkillAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_upd',
        'personal_info',
        'technology',
        'percentage',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'personal_info',
        'technology',
        'id',
        'percentage',
    )


class ContactInfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_upd',
        'location',
        'email',
        'phone',
        'coordinate',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'location',
        'email',
        'phone',
        'coordinate',
    )


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_upd',
        'name',
        'email',
        'message',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'name',
        'email',
        'message',
    )
    search_fields = ('name',)


class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_upd',
        'main_image',
        'title',
        'slogan',
        'description',
        'mini_description',
        'link',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'main_image',
        'title',
        'slogan',
        'description',
        'mini_description',
        'link',
    )
    raw_id_fields = ('technologies',)


class TechnologyAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_upd', 'name', 'image')
    list_filter = ('statut', 'date_add', 'date_upd', 'id', 'name', 'image')
    search_fields = ('name',)


class TechnologyProjectAdmin(admin.ModelAdmin):

    list_display = ('id', 'project', 'technology', 'percentage')
    list_filter = ('project', 'technology', 'id', 'percentage')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.PersonalInfo, PersonalInfoAdmin)
_register(models.PersonalSkill, PersonalSkillAdmin)
_register(models.ContactInfo, ContactInfoAdmin)
_register(models.Contact, ContactAdmin)
_register(models.Project, ProjectAdmin)
_register(models.Technology, TechnologyAdmin)
_register(models.TechnologyProject, TechnologyProjectAdmin)
