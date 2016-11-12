from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Topic)
admin.site.register(models.UserTopic)
