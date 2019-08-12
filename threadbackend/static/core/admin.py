from django.contrib import admin

from .models import Article, Issue, Email
from mce_filebrowser.admin import MCEFilebrowserAdmin

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)

admin.site.register(Article)
admin.site.register(Issue)
admin.site.register(Email)
