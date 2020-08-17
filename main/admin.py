from django.contrib import admin
from main.models import *


class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'level', 'name')
    list_filter = ('user', 'id', 'user', 'level', 'name')
    search_fields = ('name',)


class SkillModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'level', 'name', 'description')
    list_filter = (
        'user',
        'id',
        'user',
        'type',
        'level',
        'name',
        'description',
    )
    search_fields = ('name',)


class EducationModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'institution',
        'user',
        'level',
        'description',
        'start_date',
        'end_date',
    )
    list_filter = (
        'user',
        'start_date',
        'end_date',
        'id',
        'name',
        'institution',
        'user',
        'level',
        'description',
        'start_date',
        'end_date',
    )
    search_fields = ('name',)


class CourseModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'institution',
        'user',
        'level',
        'description',
        'start_date',
        'end_date',
    )
    list_filter = (
        'user',
        'start_date',
        'end_date',
        'id',
        'name',
        'institution',
        'user',
        'level',
        'description',
        'start_date',
        'end_date',
    )
    search_fields = ('name',)


class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'position',
        'company',
        'context',
        'summary',
        'start_date',
        'end_date',
        'user',
    )
    list_filter = (
        'start_date',
        'end_date',
        'user',
        'id',
        'type',
        'position',
        'company',
        'context',
        'summary',
        'start_date',
        'end_date',
        'user',
    )


class StatementModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user')
    list_filter = ('user', 'id', 'text', 'user')


class LetterModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user')
    list_filter = ('user', 'id', 'text', 'user')


class CertificationModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'authority',
        'description',
        'date',
        'user',
    )
    list_filter = (
        'date',
        'user',
        'id',
        'title',
        'authority',
        'description',
        'date',
        'user',
    )


class InterestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_filter = ('user', 'id', 'name', 'user')
    search_fields = ('name',)


class PersonModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'gender',
        'phone',
        'email',
        'website',
        'linkedin',
        'address',
        'image',
    )
    list_filter = (
        'user',
        'id',
        'user',
        'first_name',
        'last_name',
        'gender',
        'phone',
        'email',
        'website',
        'linkedin',
        'address',
        'image',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(LanguageModel, LanguageModelAdmin)
_register(SkillModel, SkillModelAdmin)
_register(EducationModel, EducationModelAdmin)
_register(CourseModel, CourseModelAdmin)
_register(ExperienceModel, ExperienceModelAdmin)
_register(StatementModel, StatementModelAdmin)
_register(LetterModel, LetterModelAdmin)
_register(CertificationModel, CertificationModelAdmin)
_register(InterestModel, InterestModelAdmin)
_register(PersonModel, PersonModelAdmin)
