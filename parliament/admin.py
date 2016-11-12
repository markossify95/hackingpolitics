from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Member)
admin.site.register(models.Speech)
admin.site.register(models.Act)
admin.site.register(models.Vote)
admin.site.register(models.Date)
admin.site.register(models.MemberAct)
