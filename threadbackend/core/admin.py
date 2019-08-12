from django.contrib import admin

from .models import Article, Issue, Email

admin.site.register(Article)
admin.site.register(Issue)
admin.site.register(Email)
