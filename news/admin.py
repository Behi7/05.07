from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Head_news)
admin.site.register(models.Popular_post)
admin.site.register(models.Comment)
admin.site.register(models.News_all)
admin.site.register(models.Mini_news)