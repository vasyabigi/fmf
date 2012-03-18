from django.contrib import admin
from django.db.models import TextField
from imperavi.widgets import ImperaviEditor


class ImperaviModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': ImperaviEditor},
    }

    class Media:
        js = (
            'js/jquery-1.7.min.js',
        )
